from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform


_io = [
    # clock
    ("clk25", 0, Pins("M9"), IOStandard("LVCMOS33")),

    # led
    ("user_led", 0, Pins("F7"), IOStandard("LVCMOS33")),

    # button
    ("user_btn", 0, Pins("P4"), IOStandard("LVCMOS33")),

    # ethernet
    ("eth_clocks", 0,
        Subsignal("tx", Pins("D1")),
        Subsignal("rx", Pins("F1")),
        IOStandard("LVCMOS33")
    ),
    ("eth", 0,
        Subsignal("rx_ctl", Pins("H1")),
        Subsignal("rx_data", Pins("F2 F4 G1 G3")),
        Subsignal("tx_ctl", Pins("E4")),
        Subsignal("tx_data", Pins("E3 E2 E1 F3")),
        IOStandard("LVCMOS33")
    ),

    ("eth_clocks", 1,
        Subsignal("tx", Pins("J1")),
        Subsignal("rx", Pins("J3")),
        IOStandard("LVCMOS33")
    ),
    ("eth", 1,
        Subsignal("rx_ctl", Pins("M3")),
        Subsignal("rx_data", Pins("L1 L3 M1 M2")),
        Subsignal("tx_ctl", Pins("E4")),
        Subsignal("tx_data", Pins("I3 K1 K2 H3")),
        IOStandard("LVCMOS33")
    ),
]

class Platform(XilinxPlatform):
    default_clk_name = "clk25"
    default_clk_period = 40.00

    def __init__(self):
        XilinxPlatform.__init__(self, "xc6slx16-2-ftg256", _io)
