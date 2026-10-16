## How it works

This is the placeholder MVP for the TT AI RV project, targeting TTSKY26d.
The submitted circuit is an 8-bit binary counter, not yet a RISC-V processor.
It validates the pin interface, simulation, physical design, and submission flow.
The planned replacement is a Chisel RV32E processor with a three-stage pipeline.

The counter increments on each rising clock edge while `ena` is high, wrapping
from 255 to 0. Active-low `rst_n` resets it synchronously on a rising edge,
including while `ena` is low. The count appears directly on `uo_out[7:0]`.
All dedicated inputs are ignored. Bidirectional pins remain inputs;
their output data and output-enable signals are zero.

## How to test

Select this project on the Tiny Tapeout demo board. Hold reset low and apply
at least one rising clock edge, then release reset. Step the clock manually
to observe 0, 1, 2, and so on on the eight output pins. After 255 comes 0.
A 1 MHz clock is the initial implementation target; a slow clock makes the
count easy to inspect using LEDs or a logic analyzer.

The automated test checks reset, counting, wraparound, disable/resume,
reset while disabled, ignored inputs, and bidirectional output enables.

## External hardware

None required beyond a clock and reset source. Optional LEDs with suitable
series resistors or a logic analyzer can display the counter outputs.
The Flash/SDRAM PMOD planned for the processor is not used by this MVP.
