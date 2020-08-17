# Colorlight 5A-75E

The Colorlight 5A-75E is an updated version of 5A-75B with 16 HUB75 ports. It also uses a Lattice ECP5-25 FPGA.

There are 2 known versions available on the market at this time:

* V6.0: undocumented for now
* V7.1: LFE5U-25F with CABGA256 package. [Detailed info](hardware_V7.1.md).

The board has the following components:

* LFE5U-25F FPGA
* 1 25Q16 serial PROM for FPGA configuration
* 2 1M x 16bit SDRAMs (on my board, they're EtronTech EM636165-6G 166MHz)
* 2 1Gb Ethernet PHYs (Broadcom B50612D, just like the RV901T)
* Tons of level shifters to translate from 3.3V to 5V signaling

The board has 1 unpopulated 4-pin connector with the JTAG signals and 1 unpopulated 2-pin connector with
GND and the 3.3V. This makes it extremely easy to connect a JTAG programmer to the board!

![JTAG connection](../5a-75b/jtag.jpg)
