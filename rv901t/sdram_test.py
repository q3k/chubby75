#!/usr/bin/env python3

from migen import *

from litex.soc.integration.soc_sdram import *
from litex.soc.integration.builder import *
from litex.soc.cores.clock import S6PLL

from litedram.modules import _TechnologyTimings
from litedram.modules import _SpeedgradeTimings
from litedram.modules import SDRAMModule
from litedram.phy import GENSDRPHY
from litedram.frontend.bist import LiteDRAMBISTGenerator, LiteDRAMBISTChecker

import platform

# CRG ----------------------------------------------------------------------------------------------

class _CRG(Module):
    def __init__(self, platform, sys_clk_freq):
        self.clock_domains.cd_sys    = ClockDomain()
        self.clock_domains.cd_sys_ps = ClockDomain()

        # # #

        clk25 = platform.request("clk25")
        platform.add_period_constraint(clk25, 1e9/25e6)

        self.submodules.pll = pll = S6PLL(speedgrade=-2)
        pll.register_clkin(clk25, 25e6)
        pll.create_clkout(self.cd_sys,    sys_clk_freq)
        pll.create_clkout(self.cd_sys_ps, sys_clk_freq, phase=270)

        self.specials += Instance("ODDR2",
            p_DDR_ALIGNMENT="NONE",
            p_INIT=0, p_SRTYPE="SYNC",
            i_D0=0, i_D1=1, i_S=0, i_R=0, i_CE=1,
            i_C0=self.cd_sys.clk, i_C1=~self.cd_sys.clk,
            o_Q=platform.request("sdram_clock"))

# SDRAM Module -------------------------------------------------------------------------------------

class M12L64322A(SDRAMModule):
    memtype = "SDR"
    # geometry
    nbanks = 4
    nrows  = 2048
    ncols  = 256
    # timings
    technology_timings = _TechnologyTimings(tREFI=64e6/4096, tWTR=(2, None), tCCD=(1, None), tRRD=(None, 10))
    speedgrade_timings = {"default": _SpeedgradeTimings(tRP=15, tRCD=15, tWR=15, tRFC=(None, 55), tFAW=None, tRAS=40)}

# SDRAMTest ----------------------------------------------------------------------------------------

class SDRAMTest(SoCSDRAM):
    def __init__(self, platform):
        sys_clk_freq = int(75e6)

        # SoCSDRAM ---------------------------------------------------------------------------------
        SoCSDRAM.__init__(self, platform, cpu_type = "vexriscv", cpu_variant = "minimal", clk_freq = sys_clk_freq, integrated_rom_size = 0x8000)

        # CRG --------------------------------------------------------------------------------------
        self.submodules.crg = _CRG(platform, sys_clk_freq)

        # SDRAM ------------------------------------------------------------------------------------
        # phy
        self.submodules.sdrphy = GENSDRPHY(platform.request("sdram"))
        # module
        sdram_module = M12L64322A(sys_clk_freq, "1:1")
        # controller
        self.register_sdram(self.sdrphy, sdram_module.geom_settings, sdram_module.timing_settings)
        # bist
        self.submodules.sdram_generator = LiteDRAMBISTGenerator(self.sdram.crossbar.get_port())
        self.submodules.sdram_checker   = LiteDRAMBISTChecker(self.sdram.crossbar.get_port())
        self.add_csr("sdram_generator")
        self.add_csr("sdram_checker")

        # Led --------------------------------------------------------------------------------------
        counter = Signal(32)
        self.sync += counter.eq(counter + 1)
        self.comb += platform.request("user_led").eq(counter[26])

# Build --------------------------------------------------------------------------------------------

def main():
    soc     = SDRAMTest(platform.Platform())
    builder = Builder(soc, output_dir="build")
    builder.build()

if __name__ == "__main__":
    main()
