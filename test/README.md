# Counter simulation

From the repository root, install `test/requirements.txt` in `.venv`, put its
`bin` directory on PATH, then run:

```sh
make -C test
python -m cocotb_tools.check_results test/results.xml
```

The test uses a 1 MHz clock and checks two rollovers, synchronous reset,
disable/resume, reset while disabled, ignored inputs, and inactive bidirectional
outputs. It only accesses wrapper ports so it also runs against the hardened
netlist using `make -C test GATES=yes`. Gate-level simulation needs the SKY130
Verilog models in PDK_ROOT and `test/gate_level_netlist.v`; the GDS workflow's
gate-level test job prepares these automatically.
