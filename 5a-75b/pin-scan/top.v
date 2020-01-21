module top #(
	parameter integer NIO = 197,
	parameter integer NMX = NIO - 1
)(
	inout [NMX:0] pads
);

	localparam
		ST_RESET = 0,
		ST_SENSE = 1,
		ST_PRE   = 2,
		ST_SEND  = 3,
		ST_WAIT  = 4,
		ST_NEXT  = 5;


	// Signals
	// -------

	// Control
	reg  [ 2:0] state;
	reg  [ 2:0] state_nxt;

	reg  [15:0] wait_cnt;

	// IO buffer
	reg  [NMX:0] pads_t;
	reg  [NMX:0] pads_o;
	wire [NMX:0] pads_i;

	reg  [NMX:0] pads_active;
	reg  [NMX:0] pads_busy;

	// UART
	wire uart_tx;
	wire [7:0] uart_data;
	wire uart_valid;
	wire uart_ack;
	wire uart_busy;

	// Clock / Reset
	wire clk;
	reg  [7:0] rst_cnt = 8'h00;
	reg  rst;


	// Control FSM
	// -----------

	always @(posedge clk)
		if (rst)
			state <= ST_RESET;
		else
			state <= state_nxt;

	always @(*)
	begin
		state_nxt = state;

		case (state)
			ST_RESET: begin
				state_nxt = ST_SENSE;
			end

			ST_SENSE: begin
				if (wait_cnt[15])
					state_nxt = ST_PRE;
			end

			ST_PRE: begin
				if (wait_cnt[15])
					state_nxt <= ST_SEND;
			end

			ST_SEND: begin
				state_nxt = ST_WAIT;
			end

			ST_WAIT: begin
				if (!uart_valid & !uart_busy)
					state_nxt = ST_NEXT;
			end

			ST_NEXT: begin
				state_nxt = ST_PRE;
			end
		endcase
	end

	always @(posedge clk)
		if ((state != ST_SENSE) && (state != ST_PRE))
			wait_cnt <= 0;
		else
			wait_cnt <= wait_cnt + 1;


	// IO buffers
	// ----------

	always @(posedge clk)
		if (rst)
			pads_active <= 1;
		else if (state == ST_NEXT)
			pads_active <= { pads_active[NMX-1:0], pads_active[NMX] };

	reg state_active;

	always @(posedge clk)
	begin
		state_active = (state == ST_PRE) || (state == ST_SEND) || (state == ST_WAIT);

`ifndef FORCE_DRIVE
		pads_t <= state_active ? (~pads_active | pads_busy) : { (NIO){1'b1} };
`else
		pads_t <= state_active ? ~pads_active : { (NIO){1'b1} };
`endif
		pads_o <= state_active ? { (NIO){uart_tx} } : 0;

		// Force PHY reset (P4)
`ifdef RESET_PHY
		pads_t[63] <= 1'b0;
		pads_o[63] <= 1'b0;
`endif
	end

	// Buffer
	BB iob[NMX:0] (
		.B(pads),
		.T(pads_t),
		.I(pads_o),
		.O(pads_i)
	);

	// Activity detector
	always @(posedge clk)
		if (rst)
			pads_busy <= 1'b0;
		else begin
			if (state == ST_SENSE)
				pads_busy <= pads_busy | ~pads_i;
			else if (state == ST_NEXT)
				pads_busy <= { pads_busy[NMX-1:0], pads_busy[NMX] };
		end

	
	// UART
	// ----

	reg [23:0] rom_array[0:255];
	reg [ 7:0] rom_addr;
	reg [23:0] rom_data;

	reg [39:0] uart_name_nxt;
	reg [ 4:0] uart_valid_nxt;

	reg [39:0] uart_name_shift;
	reg [ 4:0] uart_valid_shift;

	// Name ROM
	initial
		$readmemh("name.hex", rom_array);
	
	always @(posedge clk)
		rom_data <= rom_array[rom_addr];

	// Send logic
	always @(posedge clk)
		if (rst)
			rom_addr <= 0;
		else if (state == ST_SEND)
			rom_addr <= (rom_addr == NMX) ? 0 : (rom_addr + 1);

	always @(posedge clk)
		if (rom_data[7:0] == 8'h00) begin
			uart_name_nxt  <= { rom_data[23:8], 24'h0d0a00 };
			uart_valid_nxt <= { 5'b11110 };
		end else begin
			uart_name_nxt  <= { rom_data[23:0], 16'h0d0a };
			uart_valid_nxt <= { 5'b11111 };
		end

	always @(posedge clk)
		if (rst) begin
			uart_name_shift  <= 0;
			uart_valid_shift <= 0;
		end else begin
			if (state == ST_SEND) begin
				uart_name_shift  <= uart_name_nxt;
				uart_valid_shift <= uart_valid_nxt;
			end else if (uart_ack) begin
				uart_name_shift  <= { uart_name_shift[31:0], 8'h00 };
				uart_valid_shift <= { uart_valid_shift[3:0],  1'b0 };
			end
		end

	assign uart_data  = uart_name_shift[39:32];
	assign uart_valid = uart_valid_shift[4];

	// UART core
	uart_tx #(
		.DIV_WIDTH(12)
	) tx_I (
		.tx(uart_tx),
		.data(uart_data),
		.valid(uart_valid),
		.ack(uart_ack),
		.busy(uart_busy),
		.div(12'd536),	// 115200
		.clk(clk),
		.rst(rst)
	);


	// Clock / Reset
	// -------------

	OSCG #(
		.DIV(5)	/* 62 MHz */
	) osc_I (
		.OSC(clk)
	);

	always @(posedge clk)
		if (~rst_cnt[7])
			rst_cnt <= rst_cnt + 1;

	always @(posedge clk)
		rst <= ~rst_cnt[7];

endmodule
