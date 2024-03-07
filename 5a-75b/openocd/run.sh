openocd \
             -f /usr/share/openocd/scripts/interface/ftdi/digilent_jtag_smt2.cfg \
             -c "adapter_khz 1000; transport select jtag; jtag newtap test tap -irlen 8 -expected-id 0x41111043"

