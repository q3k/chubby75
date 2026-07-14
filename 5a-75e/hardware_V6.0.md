# Colorlight 5A-75E V6.0/V8.0 Hardware

Both V6.0 and V8.0 appear to have the same pinout.

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

#### LED Transceivers to J* mapping

Transceivers U23,U24,U28 completely cover RGB pins on J1,J2,J3,J4

Transceivers U25,U26,U27 completely cover RGB pins on J5,J6,J7,J8

Transceivers U14,U16,U18 completely cover RGB pins on	J9,J10,J11,J12

Transceivers U9,U12,U15 completely cover RGB pins on J13,J14,J15,J16

Transceivers U10,U11,U13,U17,U19,U20,U21,U22,U30,U38,U39 cover all shared pins

Address pins (A, B, C, D, E) of a pair of HUB75 connectors are shared and wired to the same transceiver. 5 address lines * 16 HUB75 connectors / 2 = 40 address lines.

Control pins (CLK, STB, OE) of a pair of HUB75 connectors are not shared and wired to different transceivers. 3 control lines * 16 HUB75 connectors = 48 control lines.

That makes 88 pins in total, which is exactly the number of pins on the 74HC245 transceivers (8 pins * 11 transceivers = 88 pins).

The RBG bits are unique per connector.

| Connector | HUB75 Pin Name | HUB75 Pin # | Buffer | Buffer Pin Name | Buffer Pin # | FPGA Pin # |
|-----------|----------------|-------------|--------|-----------------|--------------|------------|
| J1        | R0             | 1           | U28    | B0              | 18           | C4         |
| J1        | G0             | 2           | U28    | B1              | 17           | D4         |
| J1        | B0             | 3           | U28    | B2              | 16           | E4         |
| J1        | R1             | 5           | U28    | B3              | 15           | D3         |
| J1        | G1             | 6           | U28    | B4              | 14           | E3         |
| J1        | B1             | 7           | U28    | B5              | 13           | F4         |
| J1        | E              | 8           | U10    | B2              | 16           | N4         |
| J1        | A              | 9           | U17    | B4              | 14           | N5         |
| J1        | B              | 10          | U17    | B6              | 12           | N3         |
| J1        | C              | 11          | U10    | B4              | 14           | P3         |
| J1        | D              | 12          | U10    | B6              | 12           | P4         |
| J1        | CLK            | 13          | U30    | B2              | 16           | M3         |
| J1        | STB            | 14          | U39    | B4              | 14           | N1         |
| J1        | OE             | 15          | U39    | B6              | 12           | M4         |
| J2        | R0             | 1           | U28    | B6              | 12           | F3         |
| J2        | G0             | 2           | U28    | B7              | 11           | F5         |
| J2        | B0             | 3           | U24    | B0              | 18           | G3         |
| J2        | R1             | 5           | U24    | B1              | 17           | G4         |
| J2        | G1             | 6           | U24    | B2              | 16           | H3         |
| J2        | B1             | 7           | U24    | B3              | 15           | H4         |
| J2        | E              | 8           | U10    | B2              | 16           | N4         |
| J2        | A              | 9           | U17    | B4              | 14           | N5         |
| J2        | B              | 10          | U17    | B6              | 12           | N3         |
| J2        | C              | 11          | U10    | B4              | 14           | P3         |
| J2        | D              | 12          | U10    | B6              | 12           | P4         |
| J2        | CLK            | 13          | U30    | B3              | 15           | M3         |
| J2        | STB            | 14          | U39    | B5              | 13           | N1         |
| J2        | OE             | 15          | U39    | B7              | 11           | M4         |
| J3        | R0             | 1           | U24    | B4              | 14           | G5         |
| J3        | G0             | 2           | U24    | B5              | 13           | H5         |
| J3        | B0             | 3           | U24    | B6              | 12           | J5         |
| J3        | R1             | 5           | U24    | B7              | 11           | J4         |
| J3        | G1             | 6           | U23    | B0              | 18           | B1         |
| J3        | B1             | 7           | U23    | B1              | 17           | C2         |
| J3        | E              | 8           | U10    | B3              | 15           | N4         |
| J3        | A              | 9           | U17    | B5              | 13           | N5         |
| J3        | B              | 10          | U17    | B7              | 11           | N3         |
| J3        | C              | 11          | U10    | B5              | 13           | P3         |
| J3        | D              | 12          | U10    | B7              | 11           | P4         |
| J3        | CLK            | 13          | U30    | B4              | 14           | M3         |
| J3        | STB            | 14          | U30    | B0              | 18           | N1         |
| J3        | OE             | 15          | U30    | B6              | 12           | M4         |
| J4        | R0             | 1           | U23    | B2              | 16           | C1         |
| J4        | G0             | 2           | U23    | B3              | 15           | D1         |
| J4        | B0             | 3           | U23    | B4              | 14           | E2         |
| J4        | R1             | 5           | U23    | B5              | 13           | E1         |
| J4        | G1             | 6           | U23    | B6              | 12           | F2         |
| J4        | B1             | 7           | U23    | B7              | 11           | F1         |
| J4        | E              | 8           | U10    | B3              | 15           | N4         |
| J4        | A              | 9           | U17    | B5              | 13           | N5         |
| J4        | B              | 10          | U17    | B7              | 11           | N3         |
| J4        | C              | 11          | U10    | B5              | 13           | P3         |
| J4        | D              | 12          | U10    | B7              | 11           | P4         |
| J4        | CLK            | 13          | U30    | B5              | 13           | M3         |
| J4        | STB            | 14          | U30    | B1              | 17           | N1         |
| J4        | OE             | 15          | U30    | B7              | 11           | M4         |
| J5        | R0             | 1           | U27    | B0              | 18           | G2         |
| J5        | G0             | 2           | U27    | B1              | 17           | G1         |
| J5        | B0             | 3           | U27    | B2              | 16           | H2         |
| J5        | R1             | 5           | U27    | B3              | 15           | K5         |
| J5        | G1             | 6           | U27    | B4              | 14           | K4         |
| J5        | B1             | 7           | U27    | B5              | 13           | L3         |
| J5        | E              | 8           | U13    | B2              | 16           | N4         |
| J5        | A              | 9           | U11    | B2              | 16           | N5         |
| J5        | B              | 10          | U11    | B0              | 18           | N3         |
| J5        | C              | 11          | U11    | B6              | 12           | P3         |
| J5        | D              | 12          | U11    | B4              | 14           | P4         |
| J5        | CLK            | 13          | U17    | B2              | 16           | M3         |
| J5        | STB            | 14          | U10    | B0              | 18           | N1         |
| J5        | OE             | 15          | U17    | B0              | 18           | M4         |
| J6        | R0             | 1           | U27    | B6              | 12           | L4         |
| J6        | G0             | 2           | U27    | B7              | 11           | L5         |
| J6        | B0             | 3           | U26    | B0              | 18           | P2         |
| J6        | R1             | 5           | U26    | B1              | 17           | R2         |
| J6        | G1             | 6           | U26    | B2              | 16           | T2         |
| J6        | B1             | 7           | U26    | B3              | 15           | R3         |
| J6        | E              | 8           | U13    | B2              | 16           | N4         |
| J6        | A              | 9           | U11    | B2              | 16           | N5         |
| J6        | B              | 10          | U11    | B0              | 18           | N3         |
| J6        | C              | 11          | U11    | B6              | 12           | P3         |
| J6        | D              | 12          | U11    | B4              | 14           | P4         |
| J6        | CLK            | 13          | U17    | B3              | 15           | M3         |
| J6        | STB            | 14          | U10    | B1              | 17           | N1         |
| J6        | OE             | 15          | U17    | B1              | 17           | M4         |
| J7        | R0             | 1           | U26    | B4              | 14           | T3         |
| J7        | G0             | 2           | U26    | B5              | 13           | R4         |
| J7        | B0             | 3           | U26    | B6              | 12           | M5         |
| J7        | R1             | 5           | U26    | B7              | 11           | P5         |
| J7        | G1             | 6           | U25    | B0              | 18           | N6         |
| J7        | B1             | 7           | U25    | B1              | 17           | N7         |
| J7        | E              | 8           | U13    | B3              | 15           | N4         |
| J7        | A              | 9           | U11    | B3              | 15           | N5         |
| J7        | B              | 10          | U11    | B1              | 17           | N3         |
| J7        | C              | 11          | U11    | B7              | 11           | P3         |
| J7        | D              | 12          | U11    | B5              | 13           | P4         |
| J7        | CLK            | 13          | U13    | B4              | 14           | M3         |
| J7        | STB            | 14          | U13    | B0              | 18           | N1         |
| J7        | OE             | 15          | U13    | B6              | 12           | M4         |
| J8        | R0             | 1           | U25    | B2              | 16           | P7         |
| J8        | G0             | 2           | U25    | B3              | 15           | M7         |
| J8        | B0             | 3           | U25    | B4              | 14           | P8         |
| J8        | R1             | 5           | U25    | B5              | 13           | R8         |
| J8        | G1             | 6           | U25    | B6              | 12           | M8         |
| J8        | B1             | 7           | U25    | B7              | 11           | M9         |
| J8        | E              | 8           | U13    | B3              | 15           | N4         |
| J8        | A              | 9           | U11    | B3              | 15           | N5         |
| J8        | B              | 10          | U11    | B1              | 17           | N3         |
| J8        | C              | 11          | U11    | B7              | 11           | P3         |
| J8        | D              | 12          | U11    | B5              | 13           | P4         |
| J8        | CLK            | 13          | U13    | B5              | 13           | M3         |
| J8        | STB            | 14          | U13    | B1              | 17           | N1         |
| J8        | OE             | 15          | U13    | B7              | 11           | M4         |
| J9        | R0             | 1           | U18    | B1              | 17           | P11        |
| J9        | G0             | 2           | U18    | B0              | 18           | N11        |
| J9        | B0             | 3           | U18    | B2              | 16           | M11        |
| J9        | R1             | 5           | U18    | B4              | 14           | T13        |
| J9        | G1             | 6           | U18    | B3              | 15           | R12        |
| J9        | B1             | 7           | U18    | B5              | 13           | R13        |
| J9        | E              | 8           | U19    | B0              | 18           | N4         |
| J9        | A              | 9           | U21    | B0              | 18           | N5         |
| J9        | B              | 10          | U21    | B2              | 16           | N3         |
| J9        | C              | 11          | U21    | B4              | 14           | P3         |
| J9        | D              | 12          | U21    | B6              | 12           | P4         |
| J9        | CLK            | 13          | U19    | B2              | 16           | M3         |
| J9        | STB            | 14          | U19    | B4              | 14           | N1         |
| J9        | OE             | 15          | U19    | B6              | 12           | M4         |
| J10       | R0             | 1           | U18    | B7              | 11           | R14        |
| J10       | G0             | 2           | U18    | B6              | 12           | T14        |
| J10       | B0             | 3           | U16    | B0              | 18           | D16        |
| J10       | R1             | 5           | U16    | B2              | 16           | C15        |
| J10       | G1             | 6           | U16    | B1              | 17           | C16        |
| J10       | B1             | 7           | U16    | B3              | 15           | B16        |
| J10       | E              | 8           | U19    | B0              | 18           | N4         |
| J10       | A              | 9           | U21    | B0              | 18           | N5         |
| J10       | B              | 10          | U21    | B2              | 16           | N3         |
| J10       | C              | 11          | U21    | B4              | 14           | P3         |
| J10       | D              | 12          | U21    | B6              | 12           | P4         |
| J10       | CLK            | 13          | U19    | B3              | 15           | M3         |
| J10       | STB            | 14          | U19    | B5              | 13           | N1         |
| J10       | OE             | 15          | U19    | B7              | 11           | M4         |
| J11       | R0             | 1           | U16    | B5              | 13           | B15        |
| J11       | G0             | 2           | U16    | B4              | 14           | C14        |
| J11       | B0             | 3           | U16    | B6              | 12           | T15        |
| J11       | R1             | 5           | U14    | B0              | 18           | P15        |
| J11       | G1             | 6           | U16    | B7              | 11           | R15        |
| J11       | B1             | 7           | U14    | B1              | 17           | P12        |
| J11       | E              | 8           | U19    | B1              | 17           | N4         |
| J11       | A              | 9           | U21    | B1              | 17           | N5         |
| J11       | B              | 10          | U21    | B3              | 15           | N3         |
| J11       | C              | 11          | U21    | B5              | 13           | P3         |
| J11       | D              | 12          | U21    | B7              | 11           | P4         |
| J11       | CLK            | 13          | U20    | B4              | 14           | M3         |
| J11       | STB            | 14          | U20    | B2              | 16           | N1         |
| J11       | OE             | 15          | U20    | B0              | 18           | M4         |
| J12       | R0             | 1           | U14    | B3              | 15           | P13        |
| J12       | G0             | 2           | U14    | B2              | 16           | N12        |
| J12       | B0             | 3           | U14    | B4              | 14           | N13        |
| J12       | R1             | 5           | U14    | B6              | 12           | M12        |
| J12       | G1             | 6           | U14    | B5              | 13           | P14        |
| J12       | B1             | 7           | U14    | B7              | 11           | N14        |
| J12       | E              | 8           | U19    | B1              | 17           | N4         |
| J12       | A              | 9           | U21    | B1              | 17           | N5         |
| J12       | B              | 10          | U21    | B3              | 15           | N3         |
| J12       | C              | 11          | U21    | B5              | 13           | P3         |
| J12       | D              | 12          | U21    | B7              | 11           | P4         |
| J12       | CLK            | 13          | U20    | B5              | 13           | M3         |
| J12       | STB            | 14          | U20    | B3              | 15           | N1         |
| J12       | OE             | 15          | U20    | B1              | 17           | M4         |
| J13       | R0             | 1           | U09    | B1              | 17           | H15        |
| J13       | G0             | 2           | U09    | B0              | 18           | H14        |
| J13       | B0             | 3           | U09    | B2              | 16           | G16        |
| J13       | R1             | 5           | U09    | B4              | 14           | F16        |
| J13       | G1             | 6           | U09    | B3              | 15           | G15        |
| J13       | B1             | 7           | U09    | B5              | 13           | F15        |
| J13       | E              | 8           | U20    | B6              | 12           | N4         |
| J13       | A              | 9           | U22    | B6              | 12           | N5         |
| J13       | B              | 10          | U22    | B4              | 14           | N3         |
| J13       | C              | 11          | U22    | B2              | 16           | P3         |
| J13       | D              | 12          | U22    | B0              | 18           | P4         |
| J13       | CLK            | 13          | U38    | B0              | 18           | M3         |
| J13       | STB            | 14          | U38    | B2              | 16           | N1         |
| J13       | OE             | 15          | U38    | B4              | 14           | M4         |
| J14       | R0             | 1           | U09    | B7              | 11           | E15        |
| J14       | G0             | 2           | U09    | B6              | 12           | E16        |
| J14       | B0             | 3           | U12    | B0              | 18           | L12        |
| J14       | R1             | 5           | U12    | B2              | 16           | L13        |
| J14       | G1             | 6           | U12    | B1              | 17           | M14        |
| J14       | B1             | 7           | U12    | B3              | 15           | L14        |
| J14       | E              | 8           | U20    | B6              | 12           | N4         |
| J14       | A              | 9           | U22    | B6              | 12           | N5         |
| J14       | B              | 10          | U22    | B4              | 14           | N3         |
| J14       | C              | 11          | U22    | B2              | 16           | P3         |
| J14       | D              | 12          | U22    | B0              | 18           | P4         |
| J14       | CLK            | 13          | U38    | B1              | 17           | M3         |
| J14       | STB            | 14          | U38    | B3              | 15           | N1         |
| J14       | OE             | 15          | U38    | B5              | 13           | M4         |
| J15       | R0             | 1           | U12    | B5              | 13           | J13        |
| J15       | G0             | 2           | U12    | B4              | 14           | K13        |
| J15       | B0             | 3           | U12    | B6              | 12           | J12        |
| J15       | R1             | 5           | U15    | B0              | 18           | H13        |
| J15       | G1             | 6           | U12    | B7              | 11           | H12        |
| J15       | B1             | 7           | U15    | B1              | 17           | G12        |
| J15       | E              | 8           | U20    | B7              | 11           | N4         |
| J15       | A              | 9           | U22    | B7              | 11           | N5         |
| J15       | B              | 10          | U22    | B5              | 13           | N3         |
| J15       | C              | 11          | U22    | B3              | 15           | P3         |
| J15       | D              | 12          | U22    | B1              | 17           | P4         |
| J15       | CLK            | 13          | U39    | B1              | 17           | M3         |
| J15       | STB            | 14          | U39    | B3              | 15           | N1         |
| J15       | OE             | 15          | U38    | B6              | 12           | M4         |
| J16       | R0             | 1           | U15    | B3              | 15           | G14        |
| J16       | G0             | 2           | U15    | B2              | 16           | G13        |
| J16       | B0             | 3           | U15    | B4              | 14           | F12        |
| J16       | R1             | 5           | U15    | B6              | 12           | F13        |
| J16       | G1             | 6           | U15    | B5              | 13           | F14        |
| J16       | B1             | 7           | U15    | B7              | 11           | E14        |
| J16       | E              | 8           | U20    | B7              | 11           | N4         |
| J16       | A              | 9           | U22    | B7              | 11           | N5         |
| J16       | B              | 10          | U22    | B5              | 13           | N3         |
| J16       | C              | 11          | U22    | B3              | 15           | P3         |
| J16       | D              | 12          | U22    | B1              | 17           | P4         |
| J16       | CLK            | 13          | U39    | B0              | 18           | M3         |
| J16       | STB            | 14          | U39    | B2              | 16           | N1         |
| J16       | OE             | 15          | U38    | B7              | 11           | M4         |


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
