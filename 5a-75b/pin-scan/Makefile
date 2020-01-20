all: top.svf

SYNTH_SRCS=top.v uart_tx.v
SIM_SRCS=top_tb.v top.v uart_tx.v OSCG.v

top.json: $(SYNTH_SRCS) name.hex
	yosys -p 'read_verilog $(SYNTH_SRCS); synth_ecp5 -top top -abc9 -json $@'

top.config: top.json top.lpf
	nextpnr-ecp5 --25k --package CABGA381 --speed 6 --lpf top.lpf --json top.json --textcfg top.config --freq 65

top.svf: top.config
	ecppack --input $< --svf $@

name.hex top.lpf: ECP5U25Pinout.csv
	./gen_lpf.py ECP5U25Pinout.csv top.lpf name.hex

top_tb: $(SIM_SRCS)
	iverilog -I `yosys-config --datdir/ecp5/` `yosys-config --datdir/ecp5/cells_sim.v` $(SIM_SRCS) -o $@

top_tb.vcd: top_tb name.hex
	./top_tb

clean:
	rm -f *.json *.config *.svf *.vcd top_tb name.hex top.lpf
