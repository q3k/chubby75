all: build/blink.svf build/blink.bit

SYNTH_SRCS=blink.v
SIM_SRCS=blink_tb.v blink.v 

ifndef V70
	PACKAGE=CABGA381
    LFP=blink_v61.lpf
else
	PACKAGE=CABGA256
    LFP=blink_v70.lpf
endif

build/blink.json: $(SYNTH_SRCS)
	yosys -p 'read_verilog $(SYNTH_SRCS); synth_ecp5 -top blink -abc9 -json $@'

build/blink.config: build/blink.json $(LPF)
	nextpnr-ecp5 --25k --package $(PACKAGE) --speed 6 --lpf $(LFP) --json build/blink.json --textcfg build/blink.config --freq 25

build/blink.svf: build/blink.config
	ecppack --compress --input $< --svf $@

build/blink.bit: build/blink.config
	ecppack --compress --input $< --bit $@

build/blink_tb: $(SIM_SRCS)
	iverilog -I `yosys-config --datdir/ecp5/` `yosys-config --datdir/ecp5/cells_sim.v` $(SIM_SRCS) -o $@

build/blink_tb.vcd: build/blink_tb
	build/blink_tb

prog: build/blink.bit
	ecpprog -S  $<

flash: build/blink.bit
	# ERASES THE DEFAULT CONTENTS OF THE SPI FLASH!
	openFPGALoader --vid 0x0403 --pid 0x6014 --unprotect-flash -f build/blink.bit

flash_backup:
	ecpprog -R 2M colorlight_backup.bit

clean:
	rm -f build/*


