all:build/playground.svf build/playground.bit

SYNTH_SRCS=main.v

PACKAGE=CABGA256
LFP=blink_v82.lpf

build/playground.json: $(SYNTH_SRCS)
	yosys -p 'read_verilog $(SYNTH_SRCS); synth_ecp5 -top playground -abc9 -json $@'

build/playground.config: build/playground.json $(LPF)
	nextpnr-ecp5 --25k --package $(PACKAGE) --speed 6 --lpf $(LFP) --json build/playground.json --textcfg build/playground.config --freq 25

build/playground.svf: build/playground.config
	ecppack --compress --input $< --svf $@

build/playground.bit: build/playground.config
	ecppack --compress --input $< --bit $@

prog: build/playground.bit
	openFPGALoader -c usb-blaster --vid 0x09fb --pid 0x6001 build/playground.bit

flash: build/playground.bit
	# ERASES THE DEFAULT CONTENTS OF THE SPI FLASH!
	openFPGALoader -c usb-blaster --vid 0x09fb --pid 0x6001 --unprotect-flash -f build/playground.bit

clean:
	rm -f build/*
