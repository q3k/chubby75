Colorlight 5A-75E V7.1 Hardware
===============================

* [Front image](images/cl-5a-75e-v71-front.jpg)
* [Back image](images/cl-5a-75e-v71-back.jpg)

Components
----------

* Lattice ECP5 `LFE5U-25F-6BG256C` ([product page](https://www.latticesemi.com/Products/FPGAandCPLD/ECP5))
* Winbond `25Q32JVSIQ`, 32 Mbits SPI flash ([datasheet](../5a-75b/datasheets/w25q32jv_spi_revc_08302016.pdf))
* 2x Broadcom `B50612D` Gigabit Ethernet PHYs ([datasheet](../5a-75b/datasheets/B50610-DS07-RDS.pdf))
* 2x ESMT `M12L16161A-5T` 1M x 16bit 200MHz SDRAMs (organized as 1M x 32bit) ([datasheet](../5a-75b/datasheets/M12L16161A.pdf))
* 23x `74HC245T` Octal Bidirectional Transceivers (used for level translation to 5V)
* U10, U11, U13, U17 are connected to A, B, C, D, E, CLK, STB, OE for J1 to J16
* U19, U20, U21, U22 are connected to A, B, C, D, E, CLK, STB, OE for J1 to J16
* U23, U28, U24, U27, U26, U25 are connected to R0, G0, B0, R1, G1, B1 for J1 to J8 as noted below in tables
* U23, U28, U24, U27, U26, U25 can be replaced if required with 74LVC245 for inputs, Vcc & DIR will need to be isolated from solder pads
* and jumpers used for connections
* U09, U12, U14, U15, U16, U18 are connected to R0, G0, B0, R1, G1, B1 for J9 to J16 as noted below in tables
* U09, U12, U14, U15, U16, U18 can be replaced if required with 74LVC245 for inputs, Vcc & DIR will need to be isolated from solder pads
* and jumpers used for connections

Connections
===========

JTAG
----

JTAG is available on a 4-pin header next to the FPGA (U33). VCC/GND are available on a 2-pin header nearby.

| Pin | Function |
|-----|----------|
| J27 | TCK      |
| J31 | TMS      |
| J32 | TDI      |
| J30 | TDO      |
|     |          |
| J33 | *3.3V*   |
| J34 | *GND*    |

Clock
-----

A 25MHz clock is available at FPGA pin P6, and is also connected to both PHYs.

LED, Button
-----------

There is a general purpose, FPGA controlled LED (DATA_LED-) at P11, active low (FPGA pin should be set to open drain).

Additionally, there is a button (J28, KEY+) at M13. When M13 is an input, pressing the button will read low, otherwise it will read high.

SPI Flash (U31)
---------------

| Flash Pin | FPGA Pin | Function | Notes |
|-----------|----------|----------| ----- |
| 1         |  N8      | CS#      |
| 2         |  T7      | SO       |
| 3         |  -       | WP#      | Wired to 3v3
| 4         |  -       | GND      |
| 5         |  T8      | SI       |
| 6         |  N9      | SCK      |
| 7         |  -       | HOLD#    | Wired to 3v3
| 8         |  -       | VCC      | Wired to 3v3

SDRAM (U29 & U32)
-----------------

The two SDRAMs are configured as 1M x32 with the address and control signals shared and the data signals independently routed to the FPGA.

| SDRAM Signal | FPGA Pin for U29 | FPGA Pin for U32 | Notes |
|--------------|------------------|------------------|-------|
| DQ0          | B13              | E2               |
| DQ1          | A11              | E4               |
| DQ2          | B9               | D3               |
| DQ3          | C11              | E5               |
| DQ4          | C9               | A4               |
| DQ5          | C10              | D4               |
| DQ6          | E8               | C4               |
| DQ7          | B5               | D5               |
| DQ8          | B6               | D6               |
| DQ9          | A6               | E6               |
| DQ10         | A5               | D8               |
| DQ11         | B4               | A8               |
| DQ12         | C3               | B8               |
| DQ13         | B3               | B10              |
| DQ14         | B2               | B11              |
| DQ15         | A2               | E11              |
| A0           | A9               | A9               |
| A1           | E10              | E10              |
| A2           | B12              | B12              |
| A3           | D13              | D13              |
| A4           | C12              | C12              |
| A5           | D11              | D11              |
| A6           | D10              | D10              |
| A7           | E9               | E9               |
| A8           | D9               | D9               |
| A9           | B7               | B7               |
| A10/AP       | C8               | C8               |
| BA           | A7               | A7               |
| LDQM         | -                | -                | Wired to GND
| UDQM         | -                | -                | Wired to GND
| CLK          | C6               | C6               |
| CKE          | -                | -                | Wired to 3v3
| CS#          | -                | -                | Wired to GND
| RAS#         | D7               | D7               |
| CAS#         | E7               | E7               |
| WE#          | C7               | C7               |

PHY0, U3
----------

| U3 Pin  | FPGA Pin | Notes |
|---------|----------|-------|
| GTXCLK  | M2       |
| TXD[0]  | L1       |
| TXD[1]  | L3       |
| TXD[2]  | P2       |
| TXD[3]  | L4       |
| TX\_EN  | M3       |
| RXC     | M1       | Connected to ~RESET via R100
| RXD[0]  | N1       |
| RXD[1]  | M5       |
| RXD[2]  | N5       |
| RXD[3]  | M6       |
| RXD\_DV | N6       |
| MDC     | P3       |
| MDIO    | T2       |
| ~RESET  | P5       | Drives RXC via R100

PHY1, U7
----------

| U7 Pin  | FPGA Pin | Notes |
|---------|----------|-------|
| GTXCLK  | M12      |
| TXD[0]  | T14      |
| TXD[1]  | R12      |
| TXD[2]  | R13      |
| TXD[3]  | R14      |
| TX\_EN  | R15      |
| RXC     | M16      | Connected to ~RESET via R107
| RXD[0]  | P13      |
| RXD[1]  | N13      |
| RXD[2]  | P14      |
| RXD[3]  | M15      |
| RXD\_DV | L15      |
| MDC     | P3       |
| MDIO    | T2       |
| ~RESET  | P5       | Drives RXC via R107


Connector J1
--------------
| J1 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        |  F3      | U28 Pin 18
| 2     | G0        |  F1      | U28 Pin 17
| 3     | B0        |  G3      | U28 Pin 16
| 4     | *GND*     |  -       |
| 5     | R1        |  G2      | U28 Pin 15  |
| 6     | G1        |  H3      | U28 Pin 14  |
| 7     | B1        |  H5      | U28 Pin 13  |
| 8     | E         |  F15     | U13 Pin 16 (Shared with J2 pin 8)
| 9     | A         |  L2      | U10 Pin 16 (Shared with J2 pin 9)
| 10    | B         |  K1      | U10 Pin 18 (Shared with J2 pin 10)
| 11    | C         |  J5      | U10 Pin 12 (Shared with J2 pin 11)
| 12    | D         |  K2      | U10 Pin 14 (Shared with J2 pin 12)
| 13    | CLK       |  B16     | U39 Pin 14
| 14    | STB       |  J14     | U39 Pin 18
| 15    | OE        |  F12     | U39 Pin 12
| 16    | *GND*     |  -       |


Connector J2
--------------
| J2 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        |  G4      | U28 Pin 12
| 2     | G0        |  G5      | U28 Pin 11
| 3     | B0        |  J2      | U24 Pin 18
| 4     | *GND*     |  -       |
| 5     | R1        |  H2      | U24 Pin 17
| 6     | G1        |  J1      | U24 Pin 16
| 7     | B1        |  J3      | U24 Pin 15
| 8     | E         |  F15     | U13 Pin 16 (Shared with J1 pin 8)
| 9     | A         |  L2      | U10 Pin 16 (Shared with J1 pin 9)
| 10    | B         |  K1      | U10 Pin 18 (Shared with J1 pin 10)
| 11    | C         |  J5      | U10 Pin 12 (Shared with J1 pin 11)
| 12    | D         |  K2      | U10 Pin 14 (Shared with J1 pin 12)
| 13    | CLK       |  B16     | U39 Pin 13
| 14    | STB       |  J14     | U39 Pin 17
| 15    | OE        |  F12     | U39 Pin 11
| 16    | *GND*     |  -       |



Connector J3
--------------
| J3 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        |  J4      | U24 Pin 14
| 2     | G0        |  K3      | U24 Pin 13
| 3     | B0        |  G1      | U24 Pin 12
| 4     | *GND*     |  -       |
| 5     | R1        |  K4      | U24 Pin 11
| 6     | G1        |  C2      | U23 Pin 18
| 7     | B1        |  E3      | U23 Pin 17
| 8     | E         |  F15     | U13 Pin 15 (Shared with J4 pin 8)
| 9     | A         |  L2      | U10 Pin 15 (Shared with J4 pin 9)
| 10    | B         |  K1      | U10 Pin 18 (Shared with J4 pin 10)
| 11    | C         |  J5      | U10 Pin 11 (Shared with J4 pin 11)
| 12    | D         |  K2      | U10 Pin 13 (Shared with J4 pin 12)
| 13    | CLK       |  B16     | U30 Pin 14
| 14    | STB       |  J14     | U30 Pin 18
| 15    | OE        |  F12     | U30 Pin 12
| 16    | *GND*     |  -       |


Connector J4
--------------
| J4 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        |  C1      | U23 Pin 16 
| 2     | G0        |  A3      | U23 Pin 15
| 3     | B0        |  F4      | U23 Pin 14
| 4     | *GND*     |  -       |
| 5     | R1        |  E1      | U23 Pin 13
| 6     | G1        |  F5      | U23 Pin 12
| 7     | B1        |  D1      | U23 Pin 11
| 8     | E         |  F15     | U13 Pin 15 (Shared with J3 pin 8)
| 9     | A         |  L2      | U10 Pin 15 (Shared with J3 pin 9)
| 10    | B         |  K1      | U10 Pin 18 (Shared with J3 pin 10)
| 11    | C         |  J5      | U10 Pin 11 (Shared with J3 pin 11)
| 12    | D         |  K2      | U10 Pin 13 (Shared with J3 pin 12)
| 13    | CLK       |  B16     | U30 Pin 13
| 14    | STB       |  J14     | U30 Pin 18
| 15    | OE        |  F12     | U30 Pin 11
| 16    | *GND*     |  -       |


Connector J5
--------------
| J5 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        | H4       | U27 Pin 18
| 2     | G0        | K5       | U27 Pin 17
| 3     | B0        | P1       | U27 Pin 16
| 4     | *GND*     | -        |
| 5     | R1        | R1       | U27 Pin 15
| 6     | G1        | L5       | U27 Pin 14
| 7     | B1        | F2       | U27 Pin 13
| 8     | E         |  F15     | U17 Pin 16 (Shared with J6 pin 8)
| 9     | A         |  L2      | U11 Pin 16 (Shared with J6 pin 9)
| 10    | B         |  K1      | U11 Pin 18 (Shared with J6 pin 10)
| 11    | C         |  J5      | U11 Pin 12 (Shared with J6 pin 11)
| 12    | D         |  K2      | U11 Pin 14 (Shared with J6 pin 12)
| 13    | CLK       |  B16     | U17 Pin 14
| 14    | STB       |  J14     | U17 Pin 18
| 15    | OE        |  F12     | U17 Pin 12
| 16    | *GND*     |  -       |


Connector J6
--------------
| J6 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        | N3       | U27 Pin 12
| 2     | G0        | M4       | U27 Pin 11
| 3     | B0        | T4       | U26 Pin 18 
| 4     | *GND*     | -        |
| 5     | R1        | R5       | U26 Pin 17
| 6     | G1        | R3       | U26 Pin 16
| 7     | B1        | N4       | U26 Pin 15
| 8     | E         |  F15     | U17 Pin 16 (Shared with J5 pin 8)
| 9     | A         |  L2      | U11 Pin 16 (Shared with J5 pin 9)
| 10    | B         |  K1      | U11 Pin 18 (Shared with J5 pin 10)
| 11    | C         |  J5      | U11 Pin 12 (Shared with J5 pin 11)
| 12    | D         |  K2      | U11 Pin 14 (Shared with J5 pin 12)
| 13    | CLK       |  B16     | U17 Pin 13
| 14    | STB       |  J14     | U17 Pin 17
| 15    | OE        |  F12     | U17 Pin 11
| 16    | *GND*     |  -       |


Connector J7
--------------
| J7 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        | P4       | U26 Pin 14
| 2     | G0        | R2       | U26 Pin 13
| 3     | B0        | M8       | U26 Pin 12
| 4     | *GND*     | -        |
| 5     | R1        | M9       | U26 Pin 11
| 6     | G1        | T6       | U25 Pin 18
| 7     | B1        | R6       | U25 Pin 17
| 8     | E         |  F15     | U17 Pin 15 (Shared with J8 pin 8)
| 9     | A         |  L2      | U11 Pin 15 (Shared with J8 pin 9)
| 10    | B         |  K1      | U11 Pin 17 (Shared with J8 pin 10)
| 11    | C         |  J5      | U11 Pin 17 (Shared with J8 pin 11)
| 12    | D         |  K2      | U11 Pin 13 (Shared with J8 pin 12)
| 13    | CLK       |  B16     | U13 Pin 14
| 14    | STB       |  J14     | U13 Pin 18
| 15    | OE        |  F12     | U13 Pin 12
| 16    | *GND*     |  -       |



Connector J8
--------------
| J8 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        | R8       | U25 Pin 16
| 2     | G0        | R7       | U25 Pin 15
| 3     | B0        | P8       | U25 Pin 14
| 4     | *GND*     | -        |
| 5     | R1        | P7       | U25 Pin 13
| 6     | G1        | N7       | U25 Pin 12
| 7     | B1        | M7       | U25 Pin 11
| 8     | E         |  F15     | U17 Pin 15 (Shared with J7 pin 8)
| 9     | A         |  L2      | U11 Pin 15 (Shared with J7 pin 9)
| 10    | B         |  K1      | U11 Pin 17 (Shared with J7 pin 10)
| 11    | C         |  J5      | U11 Pin 17 (Shared with J7 pin 11)
| 12    | D         |  K2      | U11 Pin 13 (Shared with J7 pin 12)
| 13    | CLK       |  B16     | U13 Pin 13
| 14    | STB       |  J14     | U13 Pin 17
| 15    | OE        |  F12     | U13 Pin 11
| 16    | *GND*     |  -       |


Connector J9
--------------
| J9 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        | M11      | U18 Pin 17
| 2     | G0        | N11      | U18 Pin 18
| 3     | B0        | P12      | U18 Pin 16
| 4     | *GND*     | -        |
| 5     | R1        | K15      | U18 Pin 14
| 6     | G1        | N12      | U18 Pin 15
| 7     | B1        | L16      | U18 Pin 13
| 8     | E         | F15      | U19 Pin 16 (Shared with J10 pin 8)
| 9     | A         | L2       | U21 Pin 18 (Shared with J10 pin 9)
| 10    | B         | K1       | U21 Pin 16 (Shared with J10 pin 10)
| 11    | C         | J5       | U21 Pin 14 (Shared with J10 pin 11)
| 12    | D         | K2       | U21 Pin 12 (Shared with J10 pin 12)
| 13    | CLK       | B16      | U19 Pin 18
| 14    | STB       | J14      | U19 Pin 14
| 15    | OE        | F12      | U19 Pin 12
| 16    | *GND*     | -        |


Connector J10
--------------
|J10 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        | T13      | U18 Pin 11
| 2     | G0        | N14      | U18 Pin 12
| 3     | B0        | M14      | U16 Pin 18
| 4     | *GND*     | -        |
| 5     | R1        | P16      | U16 Pin 16
| 6     | G1        | T15      | U16 Pin 17
| 7     | B1        | L14      | U16 Pin 15
| 8     | E         | F15      | U19 Pin 16 (Shared with J9 pin 8)
| 9     | A         | L2       | U21 Pin 18 (Shared with J9 pin 9)
| 10    | B         | K1       | U21 Pin 16 (Shared with J9 pin 10)
| 11    | C         | J5       | U21 Pin 14 (Shared with J9 pin 11)
| 12    | D         | K2       | U21 Pin 12 (Shared with J9 pin 12)
| 13    | CLK       | B16      | U19 Pin 17
| 14    | STB       | J14      | U19 Pin 14
| 15    | OE        | F12      | U19 Pin 11
| 16    | *GND*     | -        |


Connector J11
--------------
|J11 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        | K16      | U16 Pin 13
| 2     | G0        | J15      | U16 Pin 14
| 3     | B0        | J16      | U16 Pin 12
| 4     | *GND*     | -        |
| 5     | R1        | J12      | U14 Pin 18
| 6     | G1        | H15      | U16 Pin 11
| 7     | B1        | G16      | U14 Pin 17
| 8     | E         | F15      | U19 Pin 15 (Shared with J12 pin 8)
| 9     | A         | L2       | U21 Pin 17 (Shared with J12 pin 9)
| 10    | B         | K1       | U21 Pin 15 (Shared with J12 pin 10)
| 11    | C         | J5       | U21 Pin 13 (Shared with J12 pin 11)
| 12    | D         | K2       | U21 Pin 11 (Shared with J12 pin 12)
| 13    | CLK       | B16      | U20 Pin 18
| 14    | STB       | J14      | U20 Pin 14
| 15    | OE        | F12      | U20 Pin 12
| 16    | *GND*     | -        |


Connector J12
--------------
|J12 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        | P15      | U14 Pin 15
| 2     | G0        | L12      | U14 Pin 16
| 3     | B0        | L13      | U14 Pin 14
| 4     | *GND*     | -        |
| 5     | R1        | D14      | U14 Pin 12
| 6     | G1        | R16      | U14 Pin 13
| 7     | B1        | E16      | U14 Pin 11
| 8     | E         | F15      | U19 Pin 15 (Shared with J11 pin 8)
| 9     | A         | L2       | U21 Pin 17 (Shared with J11 pin 9)
| 10    | B         | K1       | U21 Pin 15 (Shared with J11 pin 10)
| 11    | C         | J5       | U21 Pin 13 (Shared with J11 pin 11)
| 12    | D         | K2       | U21 Pin 11 (Shared with J11 pin 12)
| 13    | CLK       | B16      | U20 Pin 17
| 14    | STB       | J14      | U20 Pin 13
| 15    | OE        | F12      | U20 Pin 11
| 16    | *GND*     | -        |


Connector J13
--------------
|J13 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        |  H13     | U09 Pin 17
| 2     | G0        |  J13     | U09 Pin 18
| 3     | B0        |  H12     | U09 Pon 16
| 4     | *GND*     |  -       |
| 5     | R1        |  G14     | U09 Pin 14
| 6     | G1        |  H14     | U09 Pin 15
| 7     | B1        |  G15     | U09 Pin 13
| 8     | E         |  F15     | U20 Pin 16 (Shared with J14 pin 8)
| 9     | A         |  L2      | U22 Pin 18 (Shared with J14 pin 9)
| 10    | B         |  K1      | U22 Pin 16 (Shared with J14 pin 10)
| 11    | C         |  J5      | U22 Pin 14 (Shared with J14 pin 11)
| 12    | D         |  K2      | U22 Pin 12 (Shared with J14 pin 12)
| 13    | CLK       |  B16     | U38 Pin 18
| 14    | STB       |  J14     | U38 Pin 14
| 15    | OE        |  F12     | U38 Pin 12
| 16    | *GND*     |  -       |


Connector J14
--------------
|J14 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        |  E14     | U09 Pin 11
| 2     | G0        |  D16     | U09 Pin 12
| 3     | B0        |  C15     | U12 Pin 18
| 4     | *GND*     |  -       |
| 5     | R1        |  B15     | U12 Pin 16
| 6     | G1        |  C16     | U12 Pin 17
| 7     | B1        |  C14     | U12 Pin 15
| 8     | E         |  F15     | U20 Pin 16 (Shared with J13 pin 8)
| 9     | A         |  L2      | U22 Pin 18 (Shared with J13 pin 9)
| 10    | B         |  K1      | U22 Pin 16 (Shared with J13 pin 10)
| 11    | C         |  J5      | U22 Pin 14 (Shared with J13 pin 11)
| 12    | D         |  K2      | U22 Pin 12 (Shared with J13 pin 12)
| 13    | CLK       |  B16     | U38 Pin 17 
| 14    | STB       |  J14     | U38 Pin 14
| 15    | OE        |  F12     | U38 Pin 11
| 16    | *GND*     |  -       |


Connector J15
--------------
|J15 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        |  A15     | U12 Pin 13
| 2     | G0        |  F16     | U12 Pin 14
| 3     | B0        |  A14     | U12 Pin 12
| 4     | *GND*     |  -       |
| 5     | R1        |  E13     | U15 Pin 18
| 6     | G1        |  B14     | U12 Pin 11
| 7     | B1        |  A13     | U15 Pin 17
| 8     | E         |  F15     | U20 Pin 15 (Shared with J16 pin 8)
| 9     | A         |  L2      | U22 Pin 17 (Shared with J16 pin 9)
| 10    | B         |  K1      | U22 Pin 15 (Shared with J16 pin 10)
| 11    | C         |  J5      | U22 Pin 13 (Shared with J16 pin 11)
| 12    | D         |  K2      | U22 Pin 11 (Shared with J16 pin 12)
| 13    | CLK       |  B16     | U30 Pin 15
| 14    | STB       |  J14     | U39 Pin 15
| 15    | OE        |  F12     | U38 Pin 16
| 16    | *GND*     |  -       |


Connector J16
--------------
|J16 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        |  G13     | U15 Pin 15
| 2     | G0        |  G12     | U15 Pin 16
| 3     | B0        |  E15     | U15 Pin 14
| 4     | *GND*     |  -       |
| 5     | R1        |  F14     | U15 Pin 12
| 6     | G1        |  F13     | U15 Pin 13
| 7     | B1        |  C13     | U15 Pin 11
| 8     | E         |  F15     | U20 Pin 15 (Shared with J15 pin 8)
| 9     | A         |  L2      | U22 Pin 17 (Shared with J15 pin 9)
| 10    | B         |  K1      | U22 Pin 15 (Shared with J15 pin 10)
| 11    | C         |  J5      | U22 Pin 13 (Shared with J15 pin 11)
| 12    | D         |  K2      | U22 Pin 11 (Shared with J15 pin 12)
| 13    | CLK       |  B16     | U30 Pin 16
| 14    | STB       |  J14     | U39 Pin 16
| 15    | OE        |  F12     | U38 Pin 15
| 16    | *GND*     |  -       |
