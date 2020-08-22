# Colorlight 5A-75E

The Colorlight 5A-75E is an updated version of 5A-75B with 16 HUB75 ports. It also uses a Lattice ECP5-25 FPGA.

There are 2 known versions available on the market at this time:

* V6.0: LFE5U-25F with CABGA256 package. [Detailed info](hardware_V6.0.md).
* V7.1: LFE5U-25F with CABGA256 package. [Detailed info](hardware_V7.1.md).

The V6.0 board has the following components in addition to the FPGA:

* 1 2M x 32bit SDRAM (ESMT M12L64322A-5T 200MHz)
* 2 1Gb Ethernet PHYs (Realtek RTL8211FD)

The V7.1 board has the following components in addition to the FPGA:

* 2 1M x 16bit SDRAMs (on my board, they're EtronTech EM636165-6G 166MHz)
* 2 1Gb Ethernet PHYs (Broadcom B50612D, just like the RV901T)

In addition, both boards have:

* 1 25Q32JV 32Mbit SPI flash for FPGA configuration
* Tons of level shifters to translate from 3.3V to 5V signaling

The board has 1 unpopulated 4-pin connector with the JTAG signals and 1 unpopulated 2-pin connector with
GND and the 3.3V. This makes it extremely easy to connect a JTAG programmer to the board! See the detailed info for each board above for JTAG pinout.

![JTAG connection](../5a-75b/jtag.jpg)
