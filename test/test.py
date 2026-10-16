import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def counter(dut):
    dut.clk.value = 0
    dut.ena.value = 1
    dut.rst_n.value = 0
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    async def tick(expected):
        dut.clk.value = 0
        await Timer(500, unit="ns")
        dut.clk.value = 1
        await Timer(500, unit="ns")
        assert int(dut.uo_out.value) == expected
        assert int(dut.uio_oe.value) == 0
        assert int(dut.uio_out.value) == 0

    await tick(0)
    dut.rst_n.value = 1
    # Exercise two rollovers and vary unused inputs.
    for cycle in range(1, 521):
        dut.ui_in.value = cycle & 255
        dut.uio_in.value = (cycle ^ 0xA5) & 255
        await tick(cycle & 255)
    dut.ena.value = 0
    for _ in range(4):
        await tick(8)
    # Reset must work even when the design is disabled.
    dut.rst_n.value = 0
    await tick(0)
    dut.rst_n.value = 1
    await tick(0)
    dut.ena.value = 1
    await tick(1)
