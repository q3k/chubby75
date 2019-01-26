RV901T Hardware
===============

Components
----------

 - U1: **FPGA** Spartan 6, XC6SLX16, FTBGA256, speed grade 2C
 - U2: **Flash** Winbond 25Q32JV, SPI, 32Mb.
 - U100: **SDRAM** M12L64322A-5T, 512K x 32b x 4 banks (64Mb), 200MHz
 - U200: **GigE PHY** Broadcom B50512D, referred to as 'phy0' / 'top'
 - U201: **GigE PHY** Broadcom B50512D, referred to as 'phy1' / 'bottom'
 - U600-U607: 74HC245 octal buffer, 5V, direction set by FPGA
 - U608-U610: 74HC245 octal buffer, 5V, direction hardwired to output

Definitions
-----------

We define 'top', 'bottom', 'left', 'right' as relative to the FPGA orientation - ie.,
top is towards the 'A' row of balls, bottom towards 'T', left towards the '1' column of balls
and right towards '16'.

JTAG
----

The board seems to have no exposed JTAG pins. However, there are marked test pads / vias on the front of the board, underneat silkscreen, to the top-right of the FPGA.

SPI Flash
---------

The SPI flash holding the configuration memory (U2) seems to be accessible via JP5, but this was not yet tested. The flash I/Os are connected through 33Ω resistors.

| JP5 Pin | U2 Pin    |
|---------|-----------|
| 1       | CLK       |
| 2       |           |
| 3       | D0/IO1    |
| 4       |           |
| 5       |           |
| 6       |           |
| 7       | CS        |
| 8       |           |
| 9       | DI/IO0    |
| 10      | **GND**   |

Connections
===========

Clock
-----

A 25MHz clock from PHY1 is available at pin M9.

SDRAM, U100
-----------

| U100 Pin | FPGA Pin |
|----------|----------|
| DQ0      | C15      |
| DQ1      | C16      |
| DQ2      | D14      |
| DQ3      | E15      |
| DQ4      | E16      |
| DQ5      | F14      |
| DQ6      | F16      |
| DQ7      | G14      |
| DQ8      | G11      |
| DQ9      | E12      |
| DQ10     | H14      |
| DQ11     | G16      |
| DQ12     | F15      |
| DQ13     | D16      |
| DQ14     | B16      |
| DQ15     | B15      |
| DQ16     | N16      |
| DQ17     | P16      |
| DQ18     | P15      |
| DQ19     | R15      |
| DQ20     | R16      |
| DQ21     | R14      |
| DQ22     | T14      |
| DQ23     | R12      |
| DQ24     | T12      |
| DQ25     | T13      |
| DQ26     | T15      |
| DQ27     | M13      |
| DQ28     | N14      |
| DQ29     | M15      |
| DQ30     | L12      |
| DQ31     | L13      |
| A0       | L16      |
| A1       | M14      |
| A2       | M16      |
| A3       | K14      |
| A4       | J12      |
| A5       | J13      |
| A6       | J11      |
| A7       | H13      |
| A8       | H11      |
| A9       | G12      |
| A10/AP   | L14      |
| BA0      | K16      |
| BA1      | K15      |
| DQM0     | **GND**  |
| DQM1     | **GND**  |
| DQM2     | **GND**  |
| DQM3     | **GND**  |
| CLK      | K11/K12  |
| CKE      | **VCC**  |
| ~CS      | J16      |
| ~RAS     | J14      |
| ~CAS     | H15      |
| ~WE      | H16      |

PHY0, U200
----------

This PHY is hard-wired to autonegotiation, RST is hardwired to 0 and MDC/MDIO are tied off.

| U200 Pin | FPGA Pin |
|----------|----------|
| GTXCLK   | D1       |
| TXD[0]   | E3       |
| TXD[1]   | E2       |
| TXD[2]   | E1       |
| TXD[3]   | F3       |
| TX\_EN   | E4       |
| RXC      | F1       |
| RXD[0]   | F2       |
| RXD[1]   | F4       |
| RXD[2]   | G1       |
| RXD[3]   | G3       |
| RXD\_DV  | H1       |

PHY1, U201
----------

This PHY is hard-wired to autonegotiation, RST is hardwired to 0 and MDC/MDIO are tied off.

| U200 Pin | FPGA Pin | Remarks                                        |
|----------|----------|------------------------------------------------|
| GTXCLK   | J1       |                                                |
| TXD[0]   | I3       | Not driven by FPGA..?                          |
| TXD[1]   | K1       |                                                |
| TXD[2]   | K2       |                                                |
| TXD[3]   | H3       |                                                |
| TX\_EN   | E4       |                                                |
| RXC      | J3       | Can't boundary scan, have to physically trace. |
| RXD[0]   | L1       |                                                |
| RXD[1]   | L3       |                                                |
| RXD[2]   | M1       |                                                |
| RXD[3]   | M2       |                                                |
| RXD\_DV  | M3       |                                                |


Buffers
-------

All I/O Buffers are 5V. Buffers U600 to U607 have a direction pin at F13.

| F13 | Buffer Direction |
|-----|------------------|
| 0   | Output           |
| 1   | Input            |

LED, Button
-----------

There is a general purpose, FPGA controlled LED at F7, active low.

Additionally, there is a button (S1). It's not exactly clear if it's (possible to read its state)[https://github.com/q3k/chubby75/issues/8].

Connector J600
--------------

Located on bottom of board.

Pin 1 labeled with arrow on top silkscreen layer. Pins are marked alternating, ie. pin 1
is the top-right corner of the connector, pin 2 is bottom-right, pin 49 top-left and pin 50 bottom-left.

| J600 Pin| FPGA Pin | Buffer                                    | Notes               |
|---------|----------|-------------------------------------------|---------------------|
| 1       | *GND*    |                                           |                     |
| 2       | *5V*     |                                           |                     |
| 3       | *GND*    |                                           |                     |
| 4       | J6       | U610, channel 2, through R603             | Shared with J601.4  |
| 5       | *GND*    |                                           |                     |
| 6       | A11      | U608, channel 0,                          | Shared with J600.6  |
| 7       | P4       | U600, channel 7,                          |                     |
| 8       | R1       | U600, channel 6                           |                     |
| 9       | M4       | U600, channel 5                           |                     |
| 10      | L5       | U600, channel 4                           |                     |
| 11      | M5       | U600, channel 3                           |                     |
| 12      | K6       | U600, channel 2                           |                     |
| 13      | T4       | U600, channel 1                           |                     |
| 14      | P5       | U600, channel 0                           |                     |
| 15      | P6       | U604, channel 7                           |                     |
| 16      | M7       | U604, channel 6                           |                     |
| 17      | N6       | U604, channel 5                           |                     |
| 18      | M6       | U604, channel 4                           |                     |
| 19      | L7       | U604, channel 3                           |                     |
| 20      | L8       | U604, channel 2                           |                     |
| 21      | P7       | U604, channel 1                           |                     |
| 22      | N8       | U604, channel 0                           |                     |
| 23      | M12      | U601, channel 7                           |                     |
| 24      | N11      | U601, channel 6                           |                     |
| 25      | M11      | U601, channel 5                           |                     |
| 26      | M10      | U601, channel 4                           |                     |
| 27      | L10      | U601, channel 3                           |                     |
| 28      | N9       | U601, channel 2                           |                     |
| 29      | P11      | U601, channel 1                           |                     |
| 30      | T11      | U601, channel 0                           |                     |
| 31      | R9       | U605, channel 7                           |                     |
| 32      | T9       | U605, channel 6                           |                     |
| 33      | T8       | U605, channel 5                           |                     |
| 34      | R7       | U605, channel 4                           |                     |
| 35      | T7       | U605, channel 3                           |                     |
| 36      | T6       | U605, channel 2                           |                     |
| 37      | R5       | U605, channel 1                           |                     |
| 38      | T5       | U605, channel 0                           |                     |
| 39      | A12      | U608, channel 7                           | Shared with J600.39 | 
| 40      | B12      | U608, channel 6                           | Shared with J600.40 |
| 41      | A13      | U608, channel 5                           | Shared with J600.41 |
| 42      | C13      | U608, channel 4                           | Shared with J600.42 |
| 43      | A14      | U608, channel 3                           | Shared with J600.43 |
| 44      | B14      | U608, channel 2                           | Shared with J600.44 |
| 45      | C11      | U608, channel 1                           | Shared with J600.45 |
| 46      | *GND*    |                                           |                     |
| 47      | E13      | U610, channel 4, through R602             | Shared with J600.47 |
| 48      | *GND*    |                                           |                     |
| 49      | *5V*     |                                           |                     |
| 50      | *GND*    |                                           |                     |

Connector J601
--------------

Located on top of board.

| J601 Pin| FPGA Pin | Buffer                                    | Notes               |
|---------|----------|-------------------------------------------|---------------------|
| 1       | *GND*    |                                           |                     |
| 2       | *5V*     |                                           |                     |
| 3       | *GND*    |                                           |                     |
| 4       | J6       | U610, channel 3                           | Shared with J600.4  |
| 5       | *GND*    |                                           |                     |
| 6       | A11      | U609, channel 0                           | Shared with J600.6  |
| 7       | D3       | U603, channel 7                           |                     |
| 8       | C3       | U603, channel 6                           |                     |
| 9       | B3       | U603, channel 5                           |                     |
| 10      | D5       | U603, channel 4                           |                     |
| 11      | A4       | U603, channel 3                           |                     |
| 12      | B2       | U603, channel 2                           |                     |
| 13      | A2       | U603, channel 1                           |                     |
| 14      | A3       | U603, chnnael 0                           |                     |
| 15      | A5       | U607, channel 7                           |                     |
| 16      | A6       | U607, channel 6                           |                     |
| 17      | A7       | U607, channel 5                           |                     |
| 18      | A8       | U607, channel 4                           |                     |
| 19      | B8       | U607, channel 3                           |                     |
| 20      | A9       | U607, channel 2                           |                     |
| 21      | A10      | U607, channel 1                           |                     |
| 22      | B10      | U607, channel 0                           |                     |
| 23      | E11      | U602, channel 7                           |                     |
| 24      | D12      | U602, channel 6                           |                     |
| 25      | D11      | U602, channel 5                           |                     |
| 26      | E10      | U602, channel 4                           |                     |
| 27      | D9       | U602, channel 3                           |                     |
| 28      | F9       | U602, channel 2                           |                     |
| 29      | D8       | U602, channel 1                           |                     |
| 30      | E8       | U602, channel 0                           |                     |
| 31      | E7       | U606, channel 7                           |                     |
| 32      | D6       | U606, channel 6                           |                     |
| 33      | E6       | U606, channel 5                           |                     |
| 34      | C9       | U606, channel 4                           |                     |
| 35      | C8       | U606, channel 3                           |                     |
| 36      | C7       | U606, channel 2                           |                     |
| 37      | C6       | U606, channel 1                           |                     |
| 38      | B6       | U606, channel 0                           |                     |
| 39      | A12      | U609, channel 7                           | Shared with J600.39 | 
| 40      | B12      | U609, channel 6                           | Shared with J600.40 |
| 41      | A13      | U609, channel 5                           | Shared with J600.41 |
| 42      | C13      | U609, channel 4                           | Shared with J600.42 |
| 43      | A14      | U609, channel 3                           | Shared with J600.43 |
| 44      | B14      | U609, channel 2                           | Shared with J600.44 |
| 45      | C11      | U609, channel 1                           | Shared with J600.45 |
| 46      | *GND*    |                                           |                     |
| 47      | E13      | U610, channel 5                           | Shared with J600.47 |
| 48      | *GND*    |                                           |                     |
| 49      | *5V*     |                                           |                     |
| 50      | *GND*    |                                           |                     |

Connector JP4
-------------

| Pin | Connectivity             | Notes                            |
|-----|--------------------------|----------------------------------|
| 1   | *GND*                    |                                  |
| 2   | NC                       |                                  |
| 3   | FPGA H5, Unbuffered      | Used as serial TX in Migen/Litex |
| 4   | FPGA G5, Unbuffered      |                                  |
| 5   | FPGA G6, Unbuffered      | Used as serial RX in Migen/Litex |
| 6   | FPGA F5, Unbuffered      |                                  |
| 7   | FPGA F12, U610 channel 0 |                                  |
| 8   | FPGA F6, U610 channel 0  |                                  |
| 9   | *5V*                     |                                  |
| 10  | NV                       |                                  |

