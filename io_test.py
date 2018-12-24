#!/usr/bin/env python3

import csv

from migen import *
from migen.genlib.misc import WaitTimer

from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform

from litex.soc.integration.soc_core import *
from litex.soc.integration.builder import *


_io = [
    # clock
    ("clk25", 0, Pins("M9"), IOStandard("LVCMOS33")),
]


class Platform(XilinxPlatform):
    def __init__(self):
        XilinxPlatform.__init__(self, "xc6slx16-2-ftg256", _io)


def add_package_ios(platform, package_file, excludes):
    ios = []
    with open(package_file, newline="") as csvfile:
        r = csv.reader((" ".join(line.split()) for line in csvfile), delimiter=" ")
        for l in r:
            if len(l) == 4:
                io, bank, _, description = l
                if (io not in excludes) and ("IO" in description):
                    ios.append(io)
                    platform.add_extension([(io, 0, Pins(io), IOStandard("LVCMOS33"))])
    return ios


@CEInserter()
class IOIdentifier(Module):
    def __init__(self, io, identifier):
        word = Signal(32, reset=(0b1010101010101010 << 16) | identifier)
        self.comb += io.eq(word[-1])
        self.sync += word.eq(Cat(word[-1], word))


class IOtest(SoCCore):
    def __init__(self, platform):
        sys_clk_freq = int(25e6)
        SoCCore.__init__(self, platform, sys_clk_freq, cpu_type=None, with_uart=False)

        # crg
        self.submodules.crg = CRG(platform.request("clk25"))

        # create ios based on package file
        ios = add_package_ios(platform, "6slx16ftg256pkg.txt", excludes=["M9"])

        # generate a specific id on ios
        ce_timer = WaitTimer(256)
        self.submodules += ce_timer
        self.comb += ce_timer.wait.eq(~ce_timer.done)
        for i, io in enumerate(ios):
            io_identifier = IOIdentifier(platform.request(io), i)
            self.submodules += io_identifier
            self.comb += io_identifier.ce.eq(ce_timer.done)
            print("ID {:03d}: {}".format(i, io))


def main():
    soc = IOtest(Platform())
    builder = Builder(soc, output_dir="build")
    builder.build()

if __name__ == "__main__":
    main()
