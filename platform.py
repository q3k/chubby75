from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform

# IOs ----------------------------------------------------------------------------------------------

_io = [
    # clock
    ("clk25", 0, Pins("M9"), IOStandard("LVCMOS33")),

    # led
    ("user_led", 0, Pins("F7"), IOStandard("LVCMOS33")),

    # serial
    ("serial", 0,
        Subsignal("tx", Pins("H5")),
        Subsignal("rx", Pins("G6")),
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
        Subsignal("rx", Pins("K3")),
        IOStandard("LVCMOS33")
    ),
    ("eth", 1,
        Subsignal("rx_ctl", Pins("M3")),
        Subsignal("rx_data", Pins("L1 L3 M1 M2")),
        Subsignal("tx_ctl", Pins("H2")),
        Subsignal("tx_data", Pins("J3 K1 K2 H3")),
        IOStandard("LVCMOS33")
    ),

    # sdram
    ("sdram_clock", 0, Pins("K11"), IOStandard("LVCMOS33"), Misc("SLEW=FAST")),
    ("sdram_clock", 1, Pins("K12"), IOStandard("LVCMOS33"), Misc("SLEW=FAST")),
    ("sdram", 0,
        Subsignal("a", Pins("L16 M14 M16 K14 J12 J13 J11 H13 H11 G12 L14")),
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

    # Direction pin for buffers U600 to U607. 1 is input, 0 is output.
    ("bufdir", 0, Pins("F13"), IOStandard("LVCMOS33")),
]

# Connectors ---------------------------------------------------------------------------------------

_connectors = [
    # Lower connector on board. Pin 1 marked with silkscreen layer, pins then
    # alternating through the two rows of the connector.
    ("J600", {
        # Buffered through U610, shared with J601
        4: "J6",
        # Buffered through U608, shared with J601
        6: "A11",

        # Buffered through U600
        7: "P4",
        8: "R1",
        9: "M4",
        10: "L5",
        11: "M5",
        12: "K6",
        13: "T4",
        14: "P5",

        # Buffered through U604
        15: "P6",
        16: "M7",
        17: "N6",
        18: "M6",
        19: "L7",
        20: "L8",
        21: "P7",
        22: "N8",

        # Buffered through U601
        23: "M12",
        24: "N11",
        25: "M11",
        26: "M10",
        27: "L10",
        28: "N9",
        29: "P11",
        30: "T11",

        # Buffered through U605
        31: "R9",
        32: "T9",
        33: "T8",
        34: "R7",
        35: "T7",
        36: "T6",
        37: "R5",
        38: "T5",

        # Buffered through U608, shared with J601
        39: "A12",
        40: "B12",
        41: "A13",
        42: "C13",
        43: "A14",
        44: "B14",
        45: "C11",

        # Shared with J601
        47: "E13",
    }),
    # Upper connector on board. Same numbering as J600.
    ("J601", {
        # Buffered through U610, shared with J601
        4: "J6",
        # Buffered through U609, shared with J601
        6: "A11",

        # Buffered through U603
        7: "D3",
        8: "C3",
        9: "B3",
        10: "D5",
        11: "A4",
        12: "B2",
        13: "A2",
        14: "A3",

        # Buffered through U607
        15: "A5",
        16: "A6",
        17: "A7",
        18: "A8",
        19: "B8",
        20: "A9",
        21: "A10",
        22: "B10",

        # Buffered through U602
        23: "E11",
        24: "D12",
        25: "D11",
        26: "E10",
        27: "D9",
        28: "F9",
        29: "D8",
        30: "E8",

        # Buffered through U606
        31: "E7",
        32: "D6",
        33: "E6",
        34: "C9",
        35: "C8",
        36: "C7",
        37: "C6",
        38: "B6",

        # Buffered through U609, shared with J600
        39: "A12",
        40: "B12",
        41: "A13",
        42: "C13",
        43: "A14",
        44: "B14",
        45: "C11",

        # Shared with J600
        47: "E13",
    })
]

# Extension for HUB75e 'hat' (marked "Huidu Hub75E-10 Support 1/32 ")
hub75e = [
    ("hub75_control", 0,
        # bank select (a, b, c, d, e)
        Subsignal("bank", Pins("J601:42 J601:41 J601:40 J601:39 J600:6")),
        Subsignal("oe", Pins("J600:45")),
        Subsignal("stb", Pins("J601:43")),
        Subsignal("clk", Pins("J601:44")),

        IOStandard("LVCMOS33"),
    ),
    # J1
    ("hub75_chain", 0,
        Subsignal("r", Pins("J601:38 J601:35")),
        Subsignal("g", Pins("J601:37 J601:34")),
        Subsignal("b", Pins("J601:36 J601:33")),
        IOStandard("LVCMOS33"),
    ),
    # J2
    ("hub75_chain", 1,
        Subsignal("r", Pins("J601:32 J601:29")),
        Subsignal("g", Pins("J601:31 J601:28")),
        Subsignal("b", Pins("J601:30 J601:27")),
        IOStandard("LVCMOS33"),
    ),
    # J3
    ("hub75_chain", 2,
        Subsignal("r", Pins("J601:26 J601:23")),
        Subsignal("g", Pins("J601:25 J601:22")),
        Subsignal("b", Pins("J601:24 J601:21")),
        IOStandard("LVCMOS33"),
    ),
    # J4
    ("hub75_chain", 3,
        Subsignal("r", Pins("J601:20 J601:17")),
        Subsignal("g", Pins("J601:19 J601:16")),
        Subsignal("b", Pins("J601:18 J601:15")),
        IOStandard("LVCMOS33"),
    ),
    # J5
    ("hub75_chain", 4,
        Subsignal("r", Pins("J601:14 J601:11")),
        Subsignal("g", Pins("J601:13 J601:10")),
        Subsignal("b", Pins("J601:12 J601:9")),
        IOStandard("LVCMOS33"),
    ),
    # J6
    ("hub75_chain", 5,
        Subsignal("r", Pins("J600:38 J600:35")),
        Subsignal("g", Pins("J600:37 J600:34")),
        Subsignal("b", Pins("J600:36 J600:33")),
        IOStandard("LVCMOS33"),
    ),
    # J7
    ("hub75_chain", 6,
        Subsignal("r", Pins("J600:32 J600:29")),
        Subsignal("g", Pins("J600:31 J600:28")),
        Subsignal("b", Pins("J600:30 J600:27")),
        IOStandard("LVCMOS33"),
    ),
    # J8
    ("hub75_chain", 7,
        Subsignal("r", Pins("J600:26 J600:23")),
        Subsignal("g", Pins("J600:25 J600:22")),
        Subsignal("b", Pins("J600:24 J600:21")),
        IOStandard("LVCMOS33"),
    ),
    # J9
    ("hub75_chain", 8,
        Subsignal("r", Pins("J600:20 J600:17")),
        Subsignal("g", Pins("J600:19 J600:16")),
        Subsignal("b", Pins("J600:18 J600:15")),
        IOStandard("LVCMOS33"),
    ),
    # J10
    ("hub75_chain", 9,
        Subsignal("r", Pins("J600:14 J600:11")),
        Subsignal("g", Pins("J600:13 J600:10")),
        Subsignal("b", Pins("J600:12 J600:9")),
        IOStandard("LVCMOS33"),
    ),
]

# Platform -----------------------------------------------------------------------------------------

class Platform(XilinxPlatform):
    default_clk_name   = "clk25"
    default_clk_period = 1e9/25e6

    def __init__(self):
        XilinxPlatform.__init__(self, "xc6slx16-2-ftg256", _io, _connectors)
