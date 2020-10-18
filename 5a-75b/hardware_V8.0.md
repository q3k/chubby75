Colorlight 5A-75B V8.0 Hardware
===============================


Components
----------

* Lattice ECP5 `LFE5U-25F-6BG256C` ([product page](https://www.latticesemi.com/Products/FPGAandCPLD/ECP5))
* Winbond `25Q32JVSIQ`, 32 Mbits SPI flash ([datasheet](datasheets/w25q32jv_spi_revc_08302016.pdf))
* 2x Realtek `RTL8211FD` Gigabit Ethernet PHYs ([datasheet](datasheets/RTL8211F-CG-RealtekMicroelectronics.pdf))
* 1x ESMT `M12L64322A` 2M 200MHz SDRAM (organized as 4 x 512k x 32bit) ([datasheet](datasheets/M12L64322A(2S).pdf))  
* 12x `74HC245T` Octal Bidirectional Transceiver (used for level translation to 5V)


PCB overview
------------

![PCB front](images/cl-5a-75b-v80-front.jpg)
![PCB back](images/cl-5a-75b-v80-back.jpg)


Definitions
-----------


Power
-----


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


SPI Flash
---------


Connections
===========

Clock
-----

A 25MHz clock is available at FPGA pin P6, and is also connected to both PHYs.

PHY0, U11
----------

FIXME

PHY1, U13
----------

FIXME

Buffers
-------


LED, Button
-----------

There is a general purpose, FPGA controlled LED (DATA_LED-) at T6, active low (FPGA pin should be set to open drain).

Additionally, there is a button (J28, KEY+). When M13 is an input, pressing the button will read low, otherwise it will read high.

Connector J1
--------------

| J1 Pin| HUB75 pin | FPGA Pin | FPGA Bank - Pin Functions         | Buffer  | Notes           |
|-------|-----------|----------|-----------------------------------|---------|-----------------|
| 1     | R0        |  C4      |                                   |         |                 |
| 2     | G0        |  D4      |                                   |         |                 |
| 3     | B0        |  E4      |                                   |         |                 |
| 4     | *GND*     |  *GND*   | -                                 | *GND*   |                 |
| 5     | R1        |  D3      |                                   |         |                 |
| 6     | G1        |  F4      |                                   |         |                 |
| 7     | B1        |  F5      | Bank 3 - PR47D - *LRC_GPLL0C_IN*  |         |                 |
| 8     | E         |  E3      | Bank 6 - PL38A                    |         |                 |
| 9     | A         |  N5      | Bank 6 - *PL44D*                  |         |                 |
| 10    | B         |  N3      | Bank 6 - PL35D                    |         |                 |
| 11    | C         |  P3      | Bank 6 - *PL38B*                  |         |                 |
| 12    | D         |  P4      | Bank 6 - PL41A                    |         |                 |
| 13    | CLK       |  M3      | Bank 6 - PL32D                    |         |                 |
| 14    | STB       |  N1      | Bank 6 - PL32A                    |         |                 |
| 15    | OE        |  M4      | Bank 6 - PL35C                    |         |                 |
| 16    | *GND*     |  *GND*   | -                                 | *GND*   |                 |


Connector J2
--------------

| J2 Pin| HUB75 pin | FPGA Pin | FPGA Bank - Pin Functions     | Buffer  | Notes           |
|-------|-----------|----------|-------------------------------|---------|-----------------|
| 1     | R0        |  F1      |                               |         |                 |
| 2     | G0        |  F2      |                               |         |                 |
| 3     | B0        |  G2      |                               |         |                 |
| 4     | *GND*     |  *GND*   | -                             | *GND*   |                 |
| 5     | R1        |  G1      |                               |         |                 |
| 6     | G1        |  H2      |                               |         |                 |
| 7     | B1        |  H3      |                               |         |                 |
| 8     | E         |  N4      |                               |         |                 |
| 9     | A         |  N5      | Bank 6 - *PL44D*                |         |                 |
| 10    | B         |  N3      | Bank 6 - PL35D                |         |                 |
| 11    | C         |  P3      | Bank 6 - *PL38B*              |         |                 |
| 12    | D         |  P4      | Bank 6 - PL41A                |         |                 |
| 13    | CLK       |  M3      | Bank 6 - PL32D                |         |                 |
| 14    | STB       |  N1      | Bank 6 - PL32A                |         |                 |
| 15    | OE        |  M4      | Bank 6 - PL35C                |         |                 |
| 16    | *GND*     |  *GND*   | -                             | *GND*   |                 |



Connector J3
--------------

| J3 Pin| HUB75 pin | FPGA Pin | FPGA Bank - Pin Functions     | Buffer  | Notes           |
|-------|-----------|----------|-------------------------------|---------|-----------------|
| 1     | R0        |  B1      |                               |         |                 |
| 2     | G0        |  C2      |                               |         |                 |
| 3     | B0        |  C1      |                               |         |                 |
| 4     | *GND*     |  *GND*   | -                             | *GND*   |                 |
| 5     | R1        |  D1      |                               |         |                 |
| 6     | G1        |  E2      |                               |         |                 |
| 7     | B1        |  E1      |                               |         |                 |
| 8     | E         |  N4      |                               |         |                 |
| 9     | A         |  N5      | Bank 6 - *PL44D*                |         |                 |
| 10    | B         |  N3      | Bank 6 - PL35D                |         |                 |
| 11    | C         |  P3      | Bank 6 - *PL38B*              |         |                 |
| 12    | D         |  P4      | Bank 6 - PL41A                |         |                 |
| 13    | CLK       |  M3      | Bank 6 - PL32D                |         |                 |
| 14    | STB       |  N1      | Bank 6 - PL32A                |         |                 |
| 15    | OE        |  M4      | Bank 6 - PL35C                |         |                 |
| 16    | *GND*     |  *GND*   | -                             | *GND*   |                 |



Connector J4
--------------

| J4 Pin| HUB75 pin | FPGA Pin | FPGA Bank - Pin Functions     | Buffer  | Notes           |
|-------|-----------|----------|-------------------------------|---------|-----------------|
| 1     | R0        |  P5      |                               |         |                 |
| 2     | G0        |  R3      |                               |         |                 |
| 3     | B0        |  P2      |                               |         |                 |
| 4     | *GND*     |  *GND*   | -                             | *GND*   |                 |
| 5     | R1        |  R2      |                               |         |                 |
| 6     | G1        |  T2      |                               |         |                 |
| 7     | B1        |  N6      |                               |         |                 |
| 8     | E         |  N4      |                               |         |                 |
| 9     | A         |  N5      | Bank 6 - *PL44D*                |         |                 |
| 10    | B         |  N3      | Bank 6 - PL35D                |         |                 |
| 11    | C         |  P3      | Bank 6 - *PL38B*              |         |                 |
| 12    | D         |  P4      | Bank 6 - PL41A                |         |                 |
| 13    | CLK       |  M3      | Bank 6 - PL32D                |         |                 |
| 14    | STB       |  N1      | Bank 6 - PL32A                |         |                 |
| 15    | OE        |  M4      | Bank 6 - PL35C                |         |                 |
| 16    | *GND*     |  *GND*   | -                             | *GND*   |                 |


Connector J5
--------------

| J5 Pin| HUB75 pin | FPGA Pin | FPGA Bank - Pin Functions     | Buffer  | Notes           |
|-------|-----------|----------|-------------------------------|---------|-----------------|
| 1     | R0        |  T13     |                               |         |                 |
| 2     | G0        |  R12     |                               |         |                 |
| 3     | B0        |  R13     |                               |         |                 |
| 4     | *GND*     |  *GND*   | -                             | *GND*   |                 |
| 5     | R1        |  R14     |                               |         |                 |
| 6     | G1        |  T14     |                               |         |                 |
| 7     | B1        |  P12     |                               |         |                 |
| 8     | E         |  N4      |                               |         |                 |
| 9     | A         |  N5      | Bank 6 - *PL44D*                |         |                 |
| 10    | B         |  N3      | Bank 6 - PL35D                |         |                 |
| 11    | C         |  P3      | Bank 6 - *PL38B*              |         |                 |
| 12    | D         |  P4      | Bank 6 - PL41A                |         |                 |
| 13    | CLK       |  M3      | Bank 6 - PL32D                |         |                 |
| 14    | STB       |  N1      | Bank 6 - PL32A                |         |                 |
| 15    | OE        |  M4      | Bank 6 - PL35C                |         |                 |
| 16    | *GND*     |  *GND*   | -                             | *GND*   |                 |



Connector J6
--------------

| J6 Pin| HUB75 pin | FPGA Pin | FPGA Bank - Pin Functions     | Buffer  | Notes           |
|-------|-----------|----------|-------------------------------|---------|-----------------|
| 1     | R0        |  R15     |                               |         |                 |
| 2     | G0        |  T15     |                               |         |                 |
| 3     | B0        |  P13     |                               |         |                 |
| 4     | *GND*     |  *GND*   | -                             | *GND*   |                 |
| 5     | R1        |  P14     |                               |         |                 |
| 6     | G1        |  N14     |                               |         |                 |
| 7     | B1        |  H15     |                               |         |                 |
| 8     | E         |  N4      |                               |         |                 |
| 9     | A         |  N5      | Bank 6 - *PL44D*                |         |                 |
| 10    | B         |  N3      | Bank 6 - PL35D                |         |                 |
| 11    | C         |  P3      | Bank 6 - *PL38B*              |         |                 |
| 12    | D         |  P4      | Bank 6 - PL41A                |         |                 |
| 13    | CLK       |  M3      | Bank 6 - PL32D                |         |                 |
| 14    | STB       |  N1      | Bank 6 - PL32A                |         |                 |
| 15    | OE        |  M4      | Bank 6 - PL35C                |         |                 |
| 16    | *GND*     |  *GND*   | -                             | *GND*   |                 |


Connector J7
--------------

| J7 Pin| HUB75 pin | FPGA Pin | FPGA Bank - Pin Functions     | Buffer  | Notes           |
|-------|-----------|----------|-------------------------------|---------|-----------------|
| 1     | R0        |  G16     |                               |         |                 |
| 2     | G0        |  H14     |                               |         |                 |
| 3     | B0        |  G15     |                               |         |                 |
| 4     | *GND*     |  *GND*   | -                             | *GND*   |                 |
| 5     | R1        |  F15     |                               |         |                 |
| 6     | G1        |  F16     |                               |         |                 |
| 7     | B1        |  E16     |                               |         |                 |
| 8     | E         |  N4      |                               |         |                 |
| 9     | A         |  N5      | Bank 6 - *PL44D*                |         |                 |
| 10    | B         |  N3      | Bank 6 - PL35D                |         |                 |
| 11    | C         |  P3      | Bank 6 - *PL38B*              |         |                 |
| 12    | D         |  P4      | Bank 6 - PL41A                |         |                 |
| 13    | CLK       |  M3      | Bank 6 - PL32D                |         |                 |
| 14    | STB       |  N1      | Bank 6 - PL32A                |         |                 |
| 15    | OE        |  M4      | Bank 6 - PL35C                |         |                 |
| 16    | *GND*     |  *GND*   | -                             | *GND*   |                 |



Connector J8
--------------

| J8 Pin| HUB75 pin | FPGA Pin | FPGA Bank - Pin Functions     | Buffer  | Notes           |
|-------|-----------|----------|-------------------------------|---------|-----------------|
| 1     | R0        |  D16     |                               |         |                 |
| 2     | G0        |  E15     |                               |         |                 |
| 3     | B0        |  C16     |                               |         |                 |
| 4     | *GND*     |  *GND*   | -                             | *GND*   |                 |
| 5     | R1        |  B16     |                               |         |                 |
| 6     | G1        |  C15     |                               |         |                 |
| 7     | B1        |  N5      |                               |         |                 |
| 8     | E         |  N4      |                               |         |                 |
| 9     | A         |  N5      | Bank 6 - *PL44D*                |         |                 |
| 10    | B         |  N3      | Bank 6 - PL35D                |         |                 |
| 11    | C         |  P3      | Bank 6 - *PL38B*              |         |                 |
| 12    | D         |  P4      | Bank 6 - PL41A                |         |                 |
| 13    | CLK       |  M3      | Bank 6 - PL32D                |         |                 |
| 14    | STB       |  N1      | Bank 6 - PL32A                |         |                 |
| 15    | OE        |  M4      | Bank 6 - PL35C                |         |                 |
| 16    | *GND*     |  *GND*   | -                             | *GND*   |                 |
