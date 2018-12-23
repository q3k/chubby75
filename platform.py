from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform


_io = [
    # clock
    ("clk25", 0, Pins("M9"), IOStandard("LVCMOS33")),

    # led
    ("user_led", 0, Pins("F7"), IOStandard("LVCMOS33")),

    # button
    ("user_btn", 0, Pins("P4"), IOStandard("LVCMOS33")),

    # serial
    ("serial", 0,
        Subsignal("tx", Pins("X")), # FIXME
        Subsignal("rx", Pins("X")), # FIXME
        IOStandard("LVCMOS33")
    ),

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

    # sdram
    ("sdram_clock", 0, Pins("K11"), IOStandard("LVCMOS33"), Misc("SLEW=FAST")),
    ("sdram_clock", 1, Pins("K12"), IOStandard("LVCMOS33"), Misc("SLEW=FAST")),
    ("sdram", 0,
        Subsignal("a", Pins("L16 M14 M16 K14 J12 J13 J11 H13 H11 G12")),
        Subsignal("dq", Pins(
            "C15 C16 D14 E15 E16 F14 F16 G14",
            "G11 E12 H14 G16 F15 D16 B16 B15",
            "N16 P16 P15 R15 R16 R14 T14 R12",
            "T12 T13 T15 M13 N14 M15 L12 L13")),
        Subsignal("we_n", Pins("H16")),
        Subsignal("ras_n", Pins("J14")),
        Subsignal("cas_n", Pins("H15")),
        Subsignal("cs_n", Pins("J16")),
        Subsignal("ba", Pins("K16 K15")),
        IOStandard("LVCMOS33"), Misc("SLEW=FAST")
    ),
]

class Platform(XilinxPlatform):
    default_clk_name = "clk25"
    default_clk_period = 40.00

    def __init__(self):
        XilinxPlatform.__init__(self, "xc6slx16-2-ftg256", _io)
