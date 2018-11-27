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

The SPI flash holding the configuration memory (U2) seems to be accessible via JP5, but this was not yet tested.

Connections
===========

Clock
-----

A 25MHz clock from PHY1 is available at pin M9.

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
| TXD[0]   | ??       | Not driven by FPGA..?                          |
| TXD[1]   | K1       |                                                |
| TXD[2]   | K2       |                                                |
| TXD[3]   | H3       |                                                |
| TX\_EN   | E4       |                                                |
| RXC      | ??       | Can't boundary scan, have to physically trace. |
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

Additionally, there is a button at P4.

Connector J600
--------------

Located on bottom of board.

Pin 1 labeled with arrow on top silkscreen layer. Pins are marked alternating, ie. pin 1
is the top-right corner of the connector, pin 2 is bottom-right, pin 49 top-left and pin 50 bottom-left.

| ID1 Pin | FPGA Pin | Buffer                                    |
|---------|----------|-------------------------------------------|
| 1       | *GND*    |                                           |
| 2       | *5V*     |                                           |
| 3       | *GND*    |                                           |
| 4       | ???      |                                           |
| 5       | *GND*    |                                           |
| 6       | ???      |                                           |
| 7       | P4       | U600, channel 7, shared with button S1    |
| 8       | R1       | U600, channel 6                           |
| 9       | M4       | U600, channel 5                           |
| 10      | L5       | U600, channel 4                           |
| 11      | M5       | U600, channel 3                           |
| 12      | K6       | U600, channel 2                           |
| 13      | T4       | U600, channel 1                           |
| 14      | P5       | U600, channel 0                           |
| 15      | P6       | U604, channel 7                           |
| 16      | M7       | U604, channel 6                           |
| 17      | N6       | U604, channel 5                           |
| 18      | M6       | U604, channel 4                           |
| 19      | L7       | U604, channel 3                           |
| 20      | L8       | U604, channel 2                           |
| 21      | P7       | U604, channel 1                           |
| 22      | N8       | U604, channel 0                           |
| 23      | M12      | U601, channel 7                           |
| 24      | N11      | U601, channel 6                           |
| 25      | M11      | U601, channel 5                           |
| 26      | M10      | U601, channel 4                           |
| 27      | L10      | U601, channel 3                           |
| 28      | N9       | U601, channel 2                           |
| 29      | P11      | U601, channel 1                           |
| 30      | T11      | U601, channel 0                           |
| 31      | R9       | U605, channel 7                           |
| 32      | T9       | U605, channel 6                           |
| 33      | T8       | U605, channel 5                           |
| 34      | R7       | U605, channel 4                           |
| 35      | T7       | U605, channel 3                           |
| 36      | T6       | U605, channel 2                           |
| 37      | R5       | U605, channel 1                           |
| 38      | T5       | U605, channel 0                           |
| 39      | A12      | U608, channel 7                           |
| 40      | B12      | U608, channel 6                           |
| 41      | A13      | U608, channel 5                           |
| 42      | C13      | U608, channel 4                           |
| 43      | A14      | U608, channel 3                           |
| 44      | B14      | U608, channel 2                           |
| 45      | C11      | U608, channel 1                           |
| 46      | *GND*    |                                           |
| 47      | E13      | Not buffered, goes directly through R602? |
| 48      | *GND*    |                                           |
| 49      | *5V*     |                                           |
| 50      | *GND*    |                                           |
