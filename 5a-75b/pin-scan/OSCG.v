module OSCG #(
	parameter integer DIV = 0
)(
	output wire OSC
);

	reg clk = 1'b0;

	always #5 clk = ~clk;

	assign OSC = clk;

endmodule
