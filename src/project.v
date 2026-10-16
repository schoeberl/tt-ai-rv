`default_nettype none

// Submission-flow MVP; to be replaced by the Chisel RV32E implementation.
module tt_um_schoeberl_tt_ai_rv (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);
    reg [7:0] count;
    always @(posedge clk) begin
        if (!rst_n)
            count <= 8'd0;
        else if (ena)
            count <= count + 8'd1;
    end

    assign uo_out = count;
    assign uio_out = 8'd0;
    assign uio_oe = 8'd0;
    wire _unused = &{ui_in, uio_in, 1'b0};
endmodule

`default_nettype wire
