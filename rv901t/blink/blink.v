module top(
	input  wire clk25,
	output reg  user_led
	);

	reg [32:0] counter;

	always @(posedge clk25) begin
		if (counter < 12500000)
			counter <= counter + 1;
		else begin
			counter  <= 0;
			user_led <= ~user_led;
		end
	end
endmodule
