RV901T LED "Receiver Card"
=========================

<img src="doc/front.jpg" />

This repository contains bits and pieces about the RV901T HUB75 LED driver card, also known as "Receive Card". As it contains a user-reprogrammable Spartan 6 FPGA (LX16, 14k 'logic cells', 9112 LUTs) and 2x GbE, it has potential to be usable as a general purpose FPGA development board, an interface card for various purposes, or a logic analyzer.

Hardware
--------

There is [hardware documention](doc/hardware.md) available, which includes WIP information about mapping from the FPGA balls / IO into various peripherals on board and connectors.

Status
------

 - Hardware RE:
   - [X] Clocking
   - [X] LED and Button
   - [X] PHY0 and PHY1
   - [X] J600 - **few pins still missing**
   - [ ] J601
   - [ ] JP5 - SPI flash connector?
   - [ ] JP2
   - [ ] U100 - SDRAM

Acknowledgments
---------------

Thanks to Niklas Fauth for donating two boards. Thanks to carrotIndustries for assisting with the preliminary RE process at Glühweinprogrammiernacht 2018.

License
-------

[CC0](http://creativecommons.org/publicdomain/zero/1.0/") - to the extent possible under law, the person who associated CC0 with this work has waived all copyright and related or neighboring rights to this work.
