`default_nettype none

module blink(
    input  wire         osc_clk25,
    input  wire         button,
    output wire         led,
    output wire         phy_rst_
);

    reg [25:0] cntr = 0;

    always @(posedge osc_clk25)
    begin
        cntr    <= cntr + 1;
    end

    assign led = cntr[23] ^ button;
    assign phy_rst_     = 1'b1;

endmodule
