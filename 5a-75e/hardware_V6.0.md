# Colorlight 5A-75E V6.0 Hardware

* [Front image](images/cl-5a-75e-v60-front.jpg)
* [Back image](images/cl-5a-75e-v60-back.jpg)

## Components

* Lattice ECP5 `LFE5U-25F-6BG256C` ([product page](https://www.latticesemi.com/Products/FPGAandCPLD/ECP5))
* Winbond `25Q32JVSIQ`, 32 Mbits SPI flash ([datasheet](../5a-75b/datasheets/w25q32jv_spi_revc_08302016.pdf))
* 2x Realtek `RTL8211FD` Gigabit Ethernet PHYs
* 1x ESMT `M12L64322A-5T` 2M x 32bit 200MHz SDRAMs
* 23x `74HC245T` Octal Bidirectional Transceivers (used for level translation to 5V)

## Connections

### JTAG

JTAG is available on a 2x2-pin header near the SPI flash. VCC and GND are
available on a 2-pin header near the Ethernet magnetics.

| Connector | Function |
|-----------|----------|
| J27       | TCK      |
| J31       | TMS      |
| J32       | TDI      |
| J30       | TDO      |
|           |          |
| J33       | 3.3V     |
| J34       | GND      |

### Clock (Y1)

A 25MHz clock is available on FPGA pin P6. It is provided by the PHYs so it stops when they are in reset state.

| FPGA Pin | Function |
|----------|----------|
| P6       | 25MHz clock

### LED and Button

There is a general purpose, FPGA controlled LED (DATA_LED-) at FPGA pin T6,
which is active low. There is a button (J28, KEY+) on FPGA pin R7 which reads
low when the button is pressed and high otherwise.

| FPGA Pin | Function |
|----------|----------|
| T6       | LED active low
| R7       | Button active low

### SPI Flash (U31)

The SPI flash is wired to a 3v3 supply. The WP# and HOLD# signals
are connected directly to 3v3. Note that N9 is not a user IO pin
on the ECP5 but is part of the sysCONFIG block, so user code must
the USRMCLK instance to control this pin.

| FPGA Pin | Flash Pin | Function |
|----------|-----------|----------|
| N8       | 1         | CS#
| T7       | 2         | SO
| T8       | 5         | SI
| N9       | 6         | CLK

### SDRAM (U29)

The SDRAM operates on the 3v3 supply. Its CS and DQM0/1/2/3 pins are hardwired
to GND, and the CKE pin is hardwired to 3v3.

| FPGA Pin  | RAM Pin   | Function |
|-----------|-----------|----------|
| D5        | 2         | DQ0
| C5        | 4         | DQ1
| E5        | 5         | DQ2
| C6        | 7         | DQ3
| D6        | 8         | DQ4
| E6        | 10        | DQ5
| D7        | 11        | DQ6
| E7        | 13        | DQ7
| D10       | 74        | DQ8
| C11       | 76        | DQ9
| D11       | 77        | DQ10
| C12       | 79        | DQ11
| E10       | 80        | DQ12
| C13       | 82        | DQ13
| D13       | 83        | DQ14
| E11       | 85        | DQ15
| A5        | 31        | DQ16
| B4        | 33        | DQ17
| A4        | 34        | DQ18
| B3        | 36        | DQ19
| A3        | 37        | DQ20
| C3        | 39        | DQ21
| A2        | 40        | DQ22
| B2        | 42        | DQ23
| D14       | 45        | DQ24
| B14       | 47        | DQ25
| A14       | 48        | DQ26
| B13       | 50        | DQ27
| A13       | 51        | DQ28
| B12       | 53        | DQ29
| B11       | 54        | DQ30
| A11       | 56        | DQ31
| A9        | 25        | A0
| B9        | 26        | A1
| B10       | 27        | A2
| C10       | 60        | A3
| D9        | 61        | A4
| C9        | 62        | A5
| E9        | 63        | A6
| D8        | 64        | A7
| E8        | 65        | A8
| C7        | 66        | A9
| B8        | 24        | A10/AP
| B7        | 22        | BA0
| A8        | 23        | BA1
| B5        | 17        | WE#
| A6        | 18        | CAS#
| B6        | 19        | RAS#
| C8        | 68        | CLK


### PHY0, U32

The PHY IO is connected to the 3v3 supply. The MDC, MDIO, and PHYRST# lines
are common between both PHYs.

| FPGA Pin  | PHY Pin   | Function |
|-----------|-----------|----------|
| L1        | 20        | TXC
| M2        | 18        | TXD0
| M1        | 17        | TXD1
| P1        | 16        | TXD2
| R1        | 15        | TXD3
| L2        | 19        | TXCTL
| J1        | 27        | RXC
| K2        | 25        | RXD0
| J3        | 24        | RXD1
| K1        | 23        | RXD2
| K3        | 22        | RXD3
| J2        | 26        | RXCTL
| R5        | 13        | MDC
| T4        | 14        | MDIO
| R6        | 12        | PHYRST#

### PHY1, U40

The PHY IO is connected to the 3v3 supply. The MDC, MDIO, and PHYRST# lines
are common between both PHYs.

| FPGA Pin  | PHY Pin   | Function |
|-----------|-----------|----------|
| J16       | 20        | TXC
| K16       | 18        | TXD0
| J15       | 17        | TXD1
| J14       | 16        | TXD2
| K15       | 15        | TXD3
| K14       | 19        | TXCTL
| M16       | 27        | RXC
| M15       | 25        | RXD0
| R16       | 24        | RXD1
| L15       | 23        | RXD2
| L16       | 22        | RXD3
| P16       | 26        | RXCTL
| R5        | 13        | MDC
| T4        | 14        | MDIO
| R6        | 12        | PHYRST#

### LED Connectors

The LED connectors use the HUB75 pinout with five address bits (A, B, C, D, E):

| HUB75 Pin     | Function |
|---------------|----------|
| 1             | R0
| 2             | G0
| 3             | B0
| 4             | GND
| 5             | R1
| 6             | G1
| 7             | B1
| 8             | E (Shared)
| 9             | A (Shared)
| 10            | B (Shared)
| 11            | C (Shared)
| 12            | D (Shared)
| 13            | CLK (Shared)
| 14            | STB/LAT (Shared)
| 15            | OE (Shared)
| 16            | GND

For each connector, the address, CLK, STB/LAT, and OE bits are shared:

| FPGA Pin  | HUB75 Pin | Function |
|-----------|-----------|----------|
| N5        | 9         | A
| N3        | 10        | B
| P3        | 11        | C
| P4        | 12        | D
| N4        | 8         | E
| M3        | 13        | CLK
| N1        | 14        | STB
| M4        | 15        | OE

The RBG bits are unique per connector:

#### LED J1

| FPGA Pin  | HUB75 Pin | Function |
|-----------|-----------|----------|
| C4        | 1         | R0
| D4        | 2         | G0
| E4        | 3         | B0
| D3        | 5         | R1
| E3        | 6         | G1
| F4        | 7         | B1

#### LED J2

| FPGA Pin  | HUB75 Pin | Function |
|-----------|-----------|----------|
| F3        | 1         | R0
| F5        | 2         | G0
| G3        | 3         | B0
| G4        | 5         | R1
| H3        | 6         | G1
| H4        | 7         | B1

#### LED J3

| FPGA Pin  | HUB75 Pin | Function |
|-----------|-----------|----------|
| G5        | 1         | R0
| H5        | 2         | G0
| J5        | 3         | B0
| J4        | 5         | R1
| B1        | 6         | G1
| C2        | 7         | B1

#### LED J4

| FPGA Pin  | HUB75 Pin | Function |
|-----------|-----------|----------|
| C1        | 1         | R0
| D1        | 2         | G0
| E2        | 3         | B0
| E1        | 5         | R1
| F2        | 6         | G1
| F1        | 7         | B1

#### LED J5

| FPGA Pin  | HUB75 Pin | Function |
|-----------|-----------|----------|
| G2        | 1         | R0
| G1        | 2         | G0
| H2        | 3         | B0
| K5        | 5         | R1
| K4        | 6         | G1
| L3        | 7         | B1

#### LED J6

| FPGA Pin  | HUB75 Pin | Function |
|-----------|-----------|----------|
| L4        | 1         | R0
| L5        | 2         | G0
| P2        | 3         | B0
| R2        | 5         | R1
| T2        | 6         | G1
| R3        | 7         | B1

#### LED J7

| FPGA Pin  | HUB75 Pin | Function |
|-----------|-----------|----------|
| T3        | 1         | R0
| R4        | 2         | G0
| M5        | 3         | B0
| P5        | 5         | R1
| N6        | 6         | G1
| N7        | 7         | B1

#### LED J8

| FPGA Pin  | HUB75 Pin | Function |
|-----------|-----------|----------|
| P7        | 1         | R0
| M7        | 2         | G0
| P8        | 3         | B0
| R8        | 5         | R1
| M8        | 6         | G1
| M9        | 7         | B1

#### LED J9

| FPGA Pin  | HUB75 Pin | Function |
|-----------|-----------|----------|
| P11       | 1         | R0
| N11       | 2         | G0
| M11       | 3         | B0
| T13       | 5         | R1
| R12       | 6         | G1
| R13       | 7         | B1

#### LED J10

| FPGA Pin  | HUB75 Pin | Function |
|-----------|-----------|----------|
| R14       | 1         | R0
| T14       | 2         | G0
| D16       | 3         | B0
| C15       | 5         | R1
| C16       | 6         | G1
| B16       | 7         | B1

#### LED J11

| FPGA Pin  | HUB75 Pin | Function |
|-----------|-----------|----------|
| B15       | 1         | R0
| C14       | 2         | G0
| T15       | 3         | B0
| P15       | 5         | R1
| R15       | 6         | G1
| P12       | 7         | B1

#### LED J12

| FPGA Pin  | HUB75 Pin | Function |
|-----------|-----------|----------|
| P13       | 1         | R0
| N12       | 2         | G0
| N13       | 3         | B0
| M12       | 5         | R1
| P14       | 6         | G1
| N14       | 7         | B1

#### LED J13

| FPGA Pin  | HUB75 Pin | Function |
|-----------|-----------|----------|
| H15       | 1         | R0
| H14       | 2         | G0
| G16       | 3         | B0
| F16       | 5         | R1
| G15       | 6         | G1
| F15       | 7         | B1

#### LED J14

| FPGA Pin  | HUB75 Pin | Function |
|-----------|-----------|----------|
| E15       | 1         | R0
| E16       | 2         | G0
| L12       | 3         | B0
| L13       | 5         | R1
| M14       | 6         | G1
| L14       | 7         | B1

#### LED J15

| FPGA Pin  | HUB75 Pin | Function |
|-----------|-----------|----------|
| J13       | 1         | R0
| K13       | 2         | G0
| J12       | 3         | B0
| H13       | 5         | R1
| H12       | 6         | G1
| G12       | 7         | B1

#### LED J16

| FPGA Pin  | HUB75 Pin | Function |
|-----------|-----------|----------|
| G14       | 1         | R0
| G13       | 2         | G0
| F12       | 3         | B0
| F13       | 5         | R1
| F14       | 6         | G1
| E14       | 7         | B1

### Unknown and Unused Pins

The following pins are either defined in the stock configuration but their
function is not known, or are entirely unused by the stock configuration image.

All other user IO pins are documented above.

| FPGA Pin  | Function  |
|-----------|-----------|
| A7        | Unknown output
| A10       | Unknown input
| A12       | Unknown input
| A15       | Unknown output
| D12       | Unknown bidirectional
| E12       | Unknown output
| E13       | Unknown output
| K12       | Unknown output
| M6        | Unknown output
| M13       | Unknown output
| N16       | Unused
