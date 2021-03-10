RV901T Hardware
===============

Annotated PCB
-------------
<img src="front_annotated.jpg" />

Components
----------
 - U1: **FPGA** Spartan 6, XC6SLX16, FTBGA256, speed grade 2C
 - U2: **Flash** Winbond 25Q32JV, SPI, 32Mb.
   - [Datasheet](https://www.winbond.com/resource-files/w25q32jv%20revh%2001072019%20plus.pdf)
 - U100: **SDRAM** M12L64322A-5T, 512K x 32b x 4 banks (64Mb), 200MHz
   - Various SDRAM vendors such as ESMT and Winbond.
   - [ESMT Datasheet](https://www.esmt.com.tw/upload/pdf/ESMT/datasheets/M12L64322A(2S).pdf)
   - [Winbond Datasheet](https://www.datasheets360.com/pdf/-6219802484225316851)
 - U200: **GigE PHY** Broadcom B50512D, referred to as 'phy0' / 'top'
 - U201: **GigE PHY** Broadcom B50512D, referred to as 'phy1' / 'bottom'
 - U600-U607: 74HC245 octal bus transceiver, 5V, direction set by FPGA
    - [Datasheet](https://assets.nexperia.com/documents/data-sheet/74HC_HCT245.pdf)
 - U608-U610: 74HC245 octal bus transceiver, 5V, direction hardwired to output

Definitions
-----------
We define 'top', 'bottom', 'left', 'right' as relative to the FPGA orientation - ie.,
top is towards the 'A' row of balls, bottom towards 'T', left towards the '1' column of balls
and right towards '16'.

Connections
===========

Power
-----
The PCB requires a 5V power supply only. You can either use the standard 4-pin
[disk-drive Molex connector](https://en.wikipedia.org/wiki/Molex_connector#Disk_drive) on J501, or you can use
the 2 terminals of J500. The top terminal of J500 is 5V, the bottom is GND.


JTAG
----
The board has no exposed JTAG pins. However, there are marked test pads / vias on the front of the board, underneat silkscreen, to the top-right of the FPGA.
For detailed instructions on how to wire up the JTAG interface see: [Getting Started](getting_started/getting_started.md) and [Improved Getting Started](getting_started/improved_jtag_getting_started.md)

Additionaly the DONE and PROG_B pins are available on JP5

| JTAG | FPGA Pin |
|------|----------|
| TCK  | C14      |
| TDI  | C12      |
| TMS  | A15      |
| TDO  | E14      |


Buffers
-------
All I/O Buffers are 5V. 
Buffers U600 to U607 have a direction pin at F13.
Buffers U608 to U610 have are hardwired to output.

| F13 | Direction |
|-----|-----------|
| 0   | Output    |
| 1   | Input     |


Button / LED
-----------
There is a general purpose, FPGA controlled LED at F7, active low (FPGA pin should be set to open drain).

Additionally, there is a button (S1). When F7 is an input, pressing the button will read low, otherwise it will read high. Pressing the button will [also always illuminate the LED](https://github.com/q3k/chubby75/issues/8).


Clock
-----
A 25MHz clock from PHY1 is available at pin M9.


Connector JP4
-------------
For Migen/Litex: JP4 Pin3(H5) is used as serial TX
For Migen/Litex: JP4 Pin5(G6) is used as serial RX 

| Shared  | Buffer  | FPGA Pin |JP4 Pin|JP4 Pin| FPGA Pin | Buffer  | Shared |
|---------|---------|----------|-------|-------|----------|---------|--------|
| **GND** | **GND** | **GND**  | **1** | **2** |          |         |        |
| TX| Unbuffered 3v3| **H5**   | **3** | **4** | **G5**   | Unbuffered 3v3|  |
| RX| Unbuffered 3v3| **G6**   | **5** | **6** | **F5**   | Unbuffered 3v3|  |
|   | U610 chan 0   | **F12**  | **7** | **8** | **F6**   | U610 chan 1   |  |
| **5V**   | **5V** |          | **9** | **10**|          |         |        |


Connector JP5 (SPI Flash)
-------------------------
The SPI flash holding the configuration memory (U2) is accessible via JP5. The flash I/Os are unbuffered 3.3V, connected through 33Ω resistors. The PROG_B signal has to be pulled LOW to GND in order to access the SPI flash.

| Shared | U2 Pin      | FPGA Pin |JP5 Pin|JP5 Pin|FPGA Pin |U2 Pin   | Shared |
|--------|-------------|----------|-------|-------|---------|---------|--------|
| CLK    | CLK         | R11      | **1** | **2** |         |         |        |
| MISO   | DO          | P10      | **3** | **4** |         |         | **5V** |
| DONE   |             | P13      | **5** | **6** | T2      |         | PROG_B |
| CS     | CS          | T3       | **7** | **8** |         |         |        |
| MOSI   | DI          | T10      | **9** | **10**| **GND** |**GND**  |**GND** |
|        |             |          |       |       |         |         |        |
|        | /HOLD /RESET| P12      |       |       |         |         |        |
|        | /WP         | N12      |       |       |         |         |        |


Connector JP600
---------------
Located on bottom of board.

Pin 1 labeled with arrow on top silkscreen layer. Pins are marked alternating, ie. pin 1
is the top-right corner of the connector, pin 2 is bottom-right, pin 49 top-left and pin 50 bottom-left.

| Shared | Buffer       |FPGA Pin  | JP600 Pin | JP600 Pin | FPGA Pin | Buffer       | Shared |
|--------|--------------|----------|-----------|-----------|----------|--------------|--------|
| **GND**| **GND**      | **GND**  | **1**     | **2**     |          | **5V**       | **5V** |
| **GND**| **GND**      | **GND**  | **3**     | **4**     | J6       | U610, chan 2, through R603| J601.4 |
| **GND**| **GND**      | **GND**  | **5**     | **6**     | A11      | U608, chan 0 | J601.6 |
|        | U600, chan 7 | P4       | **7**     | **8**     | R1       | U600, chan 6 |        |
|        | U600, chan 5 | M4       | **9**     | **10**    | L5       | U600, chan 4 |        |
|        | U600, chan 3 | M5       | **11**    | **12**    | K6       | U600, chan 2 |        |
|        | U600, chan 1 | T4       | **13**    | **14**    | P5       | U600, chan 0 |        |
|        | U604, chan 7 | P6       | **15**    | **16**    | M7       | U604, chan 6 |        |
|        | U604, chan 5 | N6       | **17**    | **18**    | M6       | U604, chan 4 |        |
|        | U604, chan 3 | L7       | **19**    | **20**    | L8       | U604, chan 2 |        |
|        | U604, chan 1 | P7       | **21**    | **22**    | N8       | U604, chan 0 |        |
|        | U601, chan 7 | M12      | **23**    | **24**    | N11      | U601, chan 6 |        |
|        | U601, chan 5 | M11      | **25**    | **26**    | M10      | U601, chan 4 |        |
|        | U601, chan 3 | L10      | **27**    | **28**    | N9       | U601, chan 2 |        |
|        | U601, chan 1 | P11      | **29**    | **30**    | T11      | U601, chan 0 |        |
|        | U605, chan 7 | R9       | **31**    | **32**    | T9       | U605, chan 6 |        |
|        | U605, chan 5 | T8       | **33**    | **34**    | R7       | U605, chan 4 |        |
|        | U605, chan 3 | T7       | **35**    | **36**    | T6       | U605, chan 2 |        |
|        | U605, chan 1 | R5       | **37**    | **38**    | T5       | U605, chan 0 |        |
| J601.39| U608, chan 7 | A12      | **39**    | **40**    | B12      | U608, chan 6 | J601.40|
| J601.41| U608, chan 5 | A13      | **41**    | **42**    | C13      | U608, chan 4 | J601.42|
| J601.43| U608, chan 3 | A14      | **43**    | **44**    | B14      | U608, chan 2 | J601.44|
| J601.45| U608, chan 1 | C11      | **45**    | **46**    | **GND**  | **GND**      | **GND**|
| J601.47| U610, chan 4, through R602| E13| **47** | **48**| **GND**  | **GND**      | **GND**|
| **5V** | **5V**       |          | **49**    | **50**    | **GND**  | **GND**      | **GND**|


Connector J601
--------------
Located on top of board.

Pin 1 labeled with arrow on top silkscreen layer. Pins are marked alternating, ie. pin 1
is the bottom-left corner of the connector, pin 2 is upper-left, pin 49 bottom_right and pin 50 upper-right.

| Shared | Buffer       |FPGA Pin  | JP601 Pin | JP601 Pin | FPGA Pin | Buffer       | Shared |
|--------|--------------|----------|-----------|-----------|----------|--------------|--------|
| **GND**| **GND**      | **GND**  | **1**     | **2**     |          | **5V**       | **5V** |
| **GND**| **GND**      | **GND**  | **3**     | **4**     | J6       | U610, chan 3 | J600.4 |
| **GND**| **GND**      | **GND**  | **5**     | **6**     | A11      | U609, chan 0 | J600.6 |
|        | U603, chan 7 | D3       | **7**     | **8**     | C3       | U603, chan 6 |        |
|        | U603, chan 5 | B3       | **9**     | **10**    | D5       | U603, chan 4 |        |
|        | U603, chan 3 | A4       | **11**    | **12**    | B2       | U603, chan 2 |        |
|        | U603, chan 1 | A2       | **13**    | **14**    | A3       | U603, chan 0 |        |
|        | U607, chan 7 | A5       | **15**    | **16**    | A6       | U607, chan 6 |        |
|        | U607, chan 5 | A7       | **17**    | **18**    | A8       | U607, chan 4 |        |
|        | U607, chan 3 | B8       | **19**    | **20**    | A9       | U607, chan 2 |        |
|        | U607, chan 1 | A10      | **21**    | **22**    | B10      | U607, chan 0 |        |
|        | U602, chan 7 | E11      | **23**    | **24**    | D12      | U602, chan 6 |        |
|        | U602, chan 5 | D11      | **25**    | **26**    | E10      | U602, chan 4 |        |
|        | U602, chan 3 | D9       | **27**    | **28**    | F9       | U602, chan 2 |        |
|        | U602, chan 1 | D8       | **29**    | **30**    | E8       | U602, chan 0 |        |
|        | U606, chan 7 | E7       | **31**    | **32**    | D6       | U606, chan 6 |        |
|        | U606, chan 5 | E6       | **33**    | **34**    | C9       | U606, chan 4 |        |
|        | U606, chan 3 | C8       | **35**    | **36**    | C7       | U606, chan 2 |        |
|        | U606, chan 1 | C6       | **37**    | **38**    | B6       | U606, chan 0 |        |
| J600.39| U609, chan 7 | A12      | **39**    | **40**    | B12      | U609, chan 6 | J600.40|
| J600.41| U609, chan 5 | A13      | **41**    | **42**    | C13      | U609, chan 4 | J600.42|
| J600.43| U609, chan 3 | A14      | **43**    | **44**    | B14      | U609, chan 2 | J600.44|
| J600.45| U609, chan 1 | C11      | **45**    | **46**    | **GND**  | **GND**      | **GND**|
| J600.47| U610, chan 5 | E13      | **47**    | **48**    | **GND**  | **GND**      | **GND**|
| **5V** | **5V**       |          | **49**    | **50**    | **GND**  | **GND**      | **GND**|


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

| U200 Pin | FPGA Pin |
|----------|----------|
| GTXCLK   | J1       |
| TXD[0]   | J3       |
| TXD[1]   | K1       |
| TXD[2]   | K2       |
| TXD[3]   | H3       |
| TX\_EN   | H2       |
| RXC      | K3       |
| RXD[0]   | L1       |
| RXD[1]   | L3       |
| RXD[2]   | M1       |
| RXD[3]   | M2       |
| RXD\_DV  | M3       |


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


