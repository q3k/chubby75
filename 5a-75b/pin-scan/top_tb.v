module top_tb;

	genvar i;
	wire [195:0] io;

	top dut_I (
		.pads(io)
	);

	for (i=0; i<196; i=i+1)
		pullup (io[i]);

	initial begin
        # 1000000 $finish;
    end

	initial begin
		$dumpfile("top_tb.vcd");
		$dumpvars(0,top_tb);
	end

endmodule

