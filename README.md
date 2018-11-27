RV901T LED "Receiver Card"
=========================

<img src="doc/front.jpg" />

This repository contains bits and pieces about the Linsn RV901T HUB75 LED driver card, also known as a "Receiver Card". Its stock function is to receive and forward framebuffer data using a proprietary protocol (from a "Sender Card") and blit out control signals to LED panels (via shields, like a HUB75 shield).

As it contains a user-reprogrammable Spartan 6 FPGA (LX16, 14k 'logic cells', 9112 LUTs) and 2x GbE, it has potential to be usable as a general purpose FPGA development board, an interface card for various purposes, or a logic analyzer.

**Chubby75** is a project to reverse engineer, document and provide tools based on this card.

Hardware
--------

There is [hardware documention](doc/hardware.md) available, which includes WIP information about mapping from the FPGA balls / IO into various peripherals on board and connectors.

Status
------

 - Hardware RE:
   - [X] Clocking
   - [X] LED and Button
   - [X] PHY0
   - [ ] PHY1 - *partially*
   - [X] J600
   - [ ] J601
   - [ ] JP5 - SPI flash connector?
   - [ ] JP2
   - [ ] U100 - SDRAM
 - Migen integration:
   - [ ] Platform Defintion - *in progress*
 - LiteX integration
   - [ ] Sample project with PicoRV32
 - LiteEth integration:
   - [ ] Spartan 6 RGMI PHY interface - *in progress*
   - [ ] Sample project

Acknowledgments
---------------

Thanks to Niklas Fauth for donating two boards and partially tracing out the PHYs. Thanks to carrotIndustries for assisting with the preliminary RE process at Glühweinprogrammiernacht 2018.

License
-------

[CC0](http://creativecommons.org/publicdomain/zero/1.0/") - to the extent possible under law, the person who associated CC0 with this work has waived all copyright and related or neighboring rights to this work.
