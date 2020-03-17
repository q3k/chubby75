#!/usr/bin/env python3

from migen import *

from litex.soc.integration.soc_core import *
from litex.soc.integration.builder import *
from litex.soc.cores.clock import S6PLL

from liteeth.phy.s6rgmii import LiteEthPHYRGMII
from liteeth.core import LiteEthUDPIPCore
from liteeth.frontend.etherbone import LiteEthEtherbone

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
        pll.create_clkout(self.cd_sys, sys_clk_freq)

# RGMIITest ----------------------------------------------------------------------------------------

class RGMIITest(SoCMini):
    def __init__(self, platform, eth_phy=0, mac_address=0x10e2d5000000, ip_address="192.168.1.50"):
        sys_clk_freq = int(133e6)

        # SoCMini ----------------------------------------------------------------------------------
        SoCMini.__init__(self, platform, sys_clk_freq)

        # CRG --------------------------------------------------------------------------------------
        self.submodules.crg = crg = _CRG(platform, sys_clk_freq)

        # 1 Gbps Ethernet --------------------------------------------------------------------------
        # phy
        ethphy = LiteEthPHYRGMII(
            clock_pads = platform.request("eth_clocks", eth_phy),
            pads       = platform.request("eth", eth_phy))
        # core
        ethcore = LiteEthUDPIPCore(
            phy         = ethphy,
            mac_address = mac_address,
            ip_address  = ip_address,
            clk_freq    = sys_clk_freq)
        self.submodules += ethphy, ethcore
        # timing constraints
        platform.add_period_constraint(ethphy.crg.cd_eth_rx.clk, 1e9/125e6)
        platform.add_false_path_constraints(crg.cd_sys.clk, ethphy.crg.cd_eth_rx.clk)

        # Led --------------------------------------------------------------------------------------
        counter = Signal(32)
        self.sync += counter.eq(counter + 1)
        self.comb += platform.request("user_led").eq(counter[26])

# Build --------------------------------------------------------------------------------------------

def main():
    soc     = RGMIITest(platform.Platform())
    builder = Builder(soc, output_dir="build")
    builder.build()

if __name__ == "__main__":
    main()
