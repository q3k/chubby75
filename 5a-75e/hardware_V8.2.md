Colorlight 5A-75E V8.2 Hardware
===============================

* [Front image](images/cl-5a-75e-v82-front.jpg)
* [Back image](images/cl-5a-75e-v82-back.jpg)

Components
----------

* Lattice ECP5 `LFE5U-25F-7BG256I` ([product page](https://www.latticesemi.com/Products/FPGAandCPLD/ECP5))
* Gigadevices `25Q32ESIG`, 32 Mbits SPI flash ([datasheet](../5a-75b/datasheets/gd25q32e_rev1_3_20221013-1825518.pdf))
* 2x Realtek `RTL8211FP` Gigabit Ethernet PHYs ([datasheet](../5a-75b/datasheets/RTL8211F-CG-RealtekMicroelectronics.pdf), [image](../5a-75b/images/cl-5a-75b-v82-RTL8211FP.jpg)) 
* 1x ESMT `M12L64322A` 2M 200MHz SDRAM (organized as 4 x 512k x 32bit) ([datasheet](../5a-75b/datasheets/M12L64322A(2S).pdf), [image](../5a-75b/images/cl-5a-75b-v82-M12L64322A.jpg))

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

There is a general purpose, FPGA controlled LED (DATA_LED-) at T6, active low (FPGA pin should be set to open drain).

Additionally, there is a button (J28, KEY+) at R7. When R7 is an input, pressing the button will read low, otherwise it will read high.

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

SDRAM (U29)
-----------------

The SDRAM is organized as 2Mx32.

| SDRAM Signal | FPGA Pin for U29 | Notes |
|--------------|------------------|-------|
| DQ0          | D5               |
| DQ1          | C5               |
| DQ2          | E5               |
| DQ3          | C6               |
| DQ4          | D6               |
| DQ5          | E6               |
| DQ6          | D7               |
| DQ7          | E7               |
| DQ8          | D10              |
| DQ9          | C11              |
| DQ10         | D11              |
| DQ11         | C12              |
| DQ12         | E10              |
| DQ13         | C13              |
| DQ14         | D13              |
| DQ15         | E11              |
| DQ16         | A5               |
| DQ17         | B4               |
| DQ18         | A4               |
| DQ19         | B3               |
| DQ20         | A3               |
| DQ21         | C3               |
| DQ22         | A2               |
| DQ23         | B2               |
| DQ24         | D14              |
| DQ25         | B14              |
| DQ26         | A14              |
| DQ27         | B13              |
| DQ28         | A13              |
| DQ29         | B12              |
| DQ30         | B11              |
| DQ31         | A11              |
| DQM0         | B5               |
| A0           | A9               |
| A1           | B9               |
| A2           | B10              |
| A3           | C10              |
| A4           | D9               |
| A5           | C9               |
| A6           | E9               |
| A7           | D8               |
| A8           | E8               |
| A9           | C7               |
| A10/AP       | B8               |
| NC(21)       | A7
| BA0          | B7               |
| BA1          | A8               |
| LDQM         | -                | Wired to GND
| UDQM         | -                | Wired to GND
| CLK          | C8               |
| CKE          | -                | Wired to 3v3
| CS#          | -                | Wired to GND
| RAS#         | B6               |
| CAS#         | A6               |
| WE#          | B5               |

### Gigabit PHYs (U32 & U40)

PHYRstB, MDC and MDIO are shared between phy0 and phy1.

| PHY Signal | FPGA Pin for U32 | FPGA Pin for U40 | Notes |
|------------|------------------|------------------|-------|
| PHYRstB    | R6               | R6               |
| MDC        | R5               | R5               |
| MDIO       | T4               | T4               |
| TXD3       | R1               | K15              |
| TXD2       | P1               | J14              |
| TXD1       | M1               | J15              |
| TXD0       | M2               | K16              |
| TXCTL      | L2               | K14              |
| TXC        | L1               | J16              |
| RXD3       | K3               | L16              | PhyAddr0
| RXD2       | K1               | L15              | PllOff
| RXD1       | J3               | R16              | TXDly
| RXD0       | K2               | M15              | RXDly
| RXCTL      | J2               | P16              | PhyAddr1
| RXC        | J1               | M16              | PhyAddr2
| INTB       | *na*             | *na*             |



Connector J1
--------------
| J1 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        | C4       | U28 Pin 18
| 2     | G0        | D4       | U28 Pin 17
| 3     | B0        | E4       | U28 Pin 16
| 4     | *GND*     | -        |
| 5     | R1        | D3       | U28 Pin 15
| 6     | G1        | E3       | U28 Pin 14
| 7     | B1        | F4       | U28 Pin 13
| 8     | E         | N4       |
| 9     | A         | N5       |
| 10    | B         | N3       |
| 11    | C         | P3       |
| 12    | D         | P4       |
| 13    | CLK       | M3       |
| 14    | STB       | N1       |
| 15    | OE        | M4       |
| 16    | *GND*     | -        |


Connector J2
--------------
| J2 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        | F3       | U28 Pin 12
| 2     | G0        | F5       | U28 Pin 11
| 3     | B0        | G3       | U24 Pin 18
| 4     | *GND*     | -        |
| 5     | R1        | G4       | U24 Pin 17
| 6     | G1        | H3       | U24 Pin 16
| 7     | B1        | H4       | U24 Pin 15
| 8     | E         | N4       |
| 9     | A         | N5       |
| 10    | B         | N3       |
| 11    | C         | P3       |
| 12    | D         | P4       |
| 13    | CLK       | M3       |
| 14    | STB       | N1       |
| 15    | OE        | M4       |
| 16    | *GND*     | -        |



Connector J3
--------------
| J3 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        | G5       | U24 Pin 14
| 2     | G0        | H5       | U24 Pin 13
| 3     | B0        | J5       | U24 Pin 12
| 4     | *GND*     | -        |
| 5     | R1        | J4       | U24 Pin 11
| 6     | G1        | B1       | U23 Pin 18
| 7     | B1        | C2       | U23 Pin 17
| 8     | E         | N4       |
| 9     | A         | N5       |
| 10    | B         | N3       |
| 11    | C         | P3       |
| 12    | D         | P4       |
| 13    | CLK       | M3       |
| 14    | STB       | N1       |
| 15    | OE        | M4       |
| 16    | *GND*     |  -       |


Connector J4
--------------
| J4 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        | C1       | U23 Pin 16
| 2     | G0        | D1       | U23 Pin 15
| 3     | B0        | E2       | U23 Pin 14
| 4     | *GND*     | -        |
| 5     | R1        | E1       | U23 Pin 13
| 6     | G1        | F2       | U23 Pin 12
| 7     | B1        | F1       | U23 Pin 11
| 8     | E         | N4       |
| 9     | A         | N5       |
| 10    | B         | N3       |
| 11    | C         | P3       |
| 12    | D         | P4       |
| 13    | CLK       | M3       |
| 14    | STB       | N1       |
| 15    | OE        | M4       |
| 16    | *GND*     |  -       |


Connector J5
--------------
| J5 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        | G2       | U27 Pin 18
| 2     | G0        | G1       | U27 Pin 17
| 3     | B0        | H2       | U27 Pin 16
| 4     | *GND*     | -        |
| 5     | R1        | K5       | U27 Pin 15
| 6     | G1        | K4       | U27 Pin 14
| 7     | B1        | L3       | U27 Pin 13
| 8     | E         | N4       |
| 9     | A         | N5       |
| 10    | B         | N3       |
| 11    | C         | P3       |
| 12    | D         | P4       |
| 13    | CLK       | M3       |
| 14    | STB       | N1       |
| 15    | OE        | M4       |
| 16    | *GND*     |  -       |


Connector J6
--------------
| J6 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        | L4       | U27 Pin 12
| 2     | G0        | L5       | U27 Pin 11
| 3     | B0        | P2       | U26 Pin 18
| 4     | *GND*     | -        |
| 5     | R1        | R2       | U26 Pin 17
| 6     | G1        | T2       | U26 Pin 16
| 7     | B1        | R3       | U26 Pin 15
| 8     | E         | N4       |
| 9     | A         | N5       |
| 10    | B         | N3       |
| 11    | C         | P3       |
| 12    | D         | P4       |
| 13    | CLK       | M3       |
| 14    | STB       | N1       |
| 15    | OE        | M4       |
| 16    | *GND*     |  -       |


Connector J7
--------------
| J7 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        | T3       | U26 Pin 14
| 2     | G0        | R4       | U26 Pin 13
| 3     | B0        | M5       | U26 Pin 12
| 4     | *GND*     | -        |
| 5     | R1        | P5       | U26 Pin 11
| 6     | G1        | N6       | U25 Pin 18
| 7     | B1        | N7       | U25 Pin 17
| 8     | E         | N4       |
| 9     | A         | N5       |
| 10    | B         | N3       |
| 11    | C         | P3       |
| 12    | D         | P4       |
| 13    | CLK       | M3       |
| 14    | STB       | N1       |
| 15    | OE        | M4       |
| 16    | *GND*     |  -       |



Connector J8
--------------
| J8 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        | P7       | U25 Pin 16
| 2     | G0        | M7       | U25 Pin 15
| 3     | B0        | P8       | U25 Pin 14
| 4     | *GND*     | -        |
| 5     | R1        | R8       | U25 Pin 13
| 6     | G1        | M8       | U25 Pin 12
| 7     | B1        | M9       | U25 Pin 11
| 8     | E         | N4       |
| 9     | A         | N5       |
| 10    | B         | N3       |
| 11    | C         | P3       |
| 12    | D         | P4       |
| 13    | CLK       | M3       |
| 14    | STB       | N1       |
| 15    | OE        | M4       |
| 16    | *GND*     |  -       |


Connector J9
--------------
| J9 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        | P11      | U18 Pin 17
| 2     | G0        | N11      | U18 Pin 18
| 3     | B0        | M11      | U18 Pin 16
| 4     | *GND*     | -        |
| 5     | R1        | T13      | U18 Pin 14
| 6     | G1        | R12      | U18 Pin 15
| 7     | B1        | R13      | U18 Pin 13
| 8     | E         | N4       |
| 9     | A         | N5       |
| 10    | B         | N3       |
| 11    | C         | P3       |
| 12    | D         | P4       |
| 13    | CLK       | M3       |
| 14    | STB       | N1       |
| 15    | OE        | M4       |
| 16    | *GND*     | -        |


Connector J10
--------------
|J10 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        | R14      | U18 Pin 11
| 2     | G0        | T14      | U18 Pin 12
| 3     | B0        | D16      | U16 Pin 18
| 4     | *GND*     | -        |
| 5     | R1        | C15      | U16 Pin 16
| 6     | G1        | C16      | U16 Pin 17
| 7     | B1        | B16      | U16 Pin 15
| 8     | E         | N4       |
| 9     | A         | N5       |
| 10    | B         | N3       |
| 11    | C         | P3       |
| 12    | D         | P4       |
| 13    | CLK       | M3       |
| 14    | STB       | N1       |
| 15    | OE        | M4       |
| 16    | *GND*     | -        |


Connector J11
--------------
|J11 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        | B15      | U16 Pin 13
| 2     | G0        | C14      | U16 Pin 14
| 3     | B0        | T15      | U16 Pin 12
| 4     | *GND*     | -        |
| 5     | R1        | P15      | U14 Pin 18
| 6     | G1        | R15      | U16 Pin 11
| 7     | B1        | P12      |
| 8     | E         | N4       |
| 9     | A         | N5       |
| 10    | B         | N3       |
| 11    | C         | P3       |
| 12    | D         | P4       |
| 13    | CLK       | M3       |
| 14    | STB       | N1       |
| 15    | OE        | M4       |
| 16    | *GND*     | -        |


Connector J12
--------------
|J12 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        | P13      | U14 Pin 15
| 2     | G0        | N12      | U14 Pin 16
| 3     | B0        | N13      | U14 Pin 14
| 4     | *GND*     | -        |
| 5     | R1        | M12      | U14 Pin 12
| 6     | G1        | P14      | U14 Pin 13
| 7     | B1        | N14      | U14 Pin 11
| 8     | E         | N4       |
| 9     | A         | N5       |
| 10    | B         | N3       |
| 11    | C         | P3       |
| 12    | D         | P4       |
| 13    | CLK       | M3       |
| 14    | STB       | N1       |
| 15    | OE        | M4       |
| 16    | *GND*     | -        |


Connector J13
--------------
|J13 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        | H15      | U09 Pin 17
| 2     | G0        | H14      | U09 Pin 18
| 3     | B0        | G16      | U09 Pin 16
| 4     | *GND*     | -        |
| 5     | R1        | F16      | U09 Pin 14
| 6     | G1        | G15      | U09 Pin 15
| 7     | B1        | F15      | U09 Pin 13
| 8     | E         | N4       |
| 9     | A         | N5       |
| 10    | B         | N3       |
| 11    | C         | P3       |
| 12    | D         | P4       |
| 13    | CLK       | M3       |
| 14    | STB       | N1       |
| 15    | OE        | M4       | U38 Pin 14
| 16    | *GND*     | -        |


Connector J14
--------------
|J14 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        | E15      | U09 Pin 11
| 2     | G0        | E16      | U09 Pin 12
| 3     | B0        | L12      | U12 Pin 18
| 4     | *GND*     | -        |
| 5     | R1        | L13      | U12 Pin 16
| 6     | G1        | M14      | U12 Pin 17
| 7     | B1        | L14      | U12 Pin 15
| 8     | E         | N4       |
| 9     | A         | N5       |
| 10    | B         | N3       |
| 11    | C         | P3       |
| 12    | D         | P4       |
| 13    | CLK       | M3       |
| 14    | STB       | N1       |
| 15    | OE        | M4       | U38 Pin 13
| 16    | *GND*     |  -       |


Connector J15
--------------
|J15 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        | J13      | U12 Pin 13
| 2     | G0        | K13      | U12 Pin 14
| 3     | B0        | J12      | U12 Pin 12
| 4     | *GND*     | -        |
| 5     | R1        | H13      | U15 Pin 18
| 6     | G1        | H12      | U12 Pin 11
| 7     | B1        | G12      | U15 Pin 17
| 8     | E         | N4       |
| 9     | A         | N5       |
| 10    | B         | N3       |
| 11    | C         | P3       |
| 12    | D         | P4       |
| 13    | CLK       | M3       |
| 14    | STB       | N1       |
| 15    | OE        | M4       | U38 Pin 12
| 16    | *GND*     |  -       |


Connector J16
--------------
|J16 Pin| HUB75 pin | FPGA Pin | Buffer & Pin|
|-------|-----------|----------|-------------|
| 1     | R0        | G14      | U15 Pin 15
| 2     | G0        | G13      | U15 Pin 16
| 3     | B0        | F12      | U15 Pin 14
| 4     | *GND*     | -        |
| 5     | R1        | F13      | U15 Pin 12
| 6     | G1        | F14      | U15 Pin 13
| 7     | B1        | E14      | U15 Pin 11
| 8     | E         | N4       |
| 9     | A         | N5       |
| 10    | B         | N3       |
| 11    | C         | P3       |
| 12    | D         | P4       |
| 13    | CLK       | M3       |
| 14    | STB       | N1       |
| 15    | OE        | M4       | U38 Pin 11
| 16    | *GND*     |  -       |
