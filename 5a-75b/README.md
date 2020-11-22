
# Colorlight 5A-75B

The Colorlight 5A-75B is an evolution of the RV901T with 8 HUB75 ports that
uses a Lattice ECP5-25 FPGA.

This makes the board extremely interesting because it's supported by the Yosys and NextPnR
open-source backend flows.

There are 3 known versions on available on the market at this time:

* V6.1: LFE5U-25F with CABGA381 package. [Detailed info](hardware_V6.1.md).
* V7.0: LFE5U-25F with CABGA256 package. [Detailed info](hardware_V7.0.md).
* V8.0: LFE5U-25F with CABGA256 package. [Detailed info](hardware_V8.0.md).

They're more or less identical in terms of peripheral components, but the connections to the FPGA pins are obviously different.

The board has the following components:

* LFE5U-25F FPGA
* 1 25Q16 serial PROM for FPGA configuration
* 2 1M x 16bit SDRAMs (on my board, they're EtronTech EM636165-6G 166MHz)
* 2 1Gb Ethernet PHYs (Broadcom B50612D, just like the RV901T)
* Tons of level shifters to translate from 3.3V to 5V signaling

The board has 1 unpopulated 4-pin connector with the JTAG signals and 1 unpopulated 2-pin connector with
GND and the 3.3V. This makes it extremely easy to connect a JTAG programmer to the board!

![JTAG connection](./jtag.jpg)

![OpenOCD detect ECP5 FPGA](./openocd.png)

