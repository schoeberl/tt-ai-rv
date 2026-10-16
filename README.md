# tt-ai-rv
Build a RV for the next Tiny Tapeout with CodeX from my iPad only

The project targets a Chisel RV32E core for a SKY130 Tiny Tapeout, aiming to use
as few tiles as possible with external memory via the Tiny Tapeout Flash/SDRAM PMOD.

## Tapeout target and local tools

Target: **TTSKY26d**, the next open SKY130 run as of October 17, 2026.
The [published submission deadline](https://tinytapeout.com/chips/) is November 30,
2026; shuttle dates and staging configurations may change.

LibreLane is a pinned Git submodule in `tools/librelane`. Initialize it with:

```sh
git submodule update --init --recursive
source flow/toolchain.env
export PDK_ROOT="$PWD/pdk"
nix-shell tools/librelane/shell.nix
```

The version pins in `flow/toolchain.env` come from the shuttle's
[machine-readable configuration](https://github.com/TinyTapeout/tinytapeout-sky-26d-staging/blob/4afb9a37ccb8adfc7ca759648c7f0feaccc03798/.github/config/librelane.txt):
LibreLane **3.0.0.dev40**, PDK **sky130A**, and SKY130 revision
`8afc8346a57fe1ab7934ba5a6056ea8b43078e71`.
The staging `BUILDING.md` lists a different, older PDK revision; we use the
machine-readable configuration for both pins rather than mixing revisions.

Inside the Nix shell, install and activate the pinned PDK using Ciel:

```sh
ciel enable --pdk sky130 "$SKY130_PDK_VERSION"
librelane --smoke-test
```

Nix and Ciel may download substantial tool and PDK data. The PDK and generated
runs are ignored by Git. The smoke test checks tool installation; project area
estimates will require generated RTL and a Tiny Tapeout floorplan configuration.
No core hardening or area estimate has been run yet.

## Counter submission MVP

The current submission is an **8-bit counter** using one `1x1` tile. The RISC-V
core and memory interface are future work. This first MVP uses Verilog directly;
we will replace it with generated RTL when adding the Chisel implementation.

- `src/project.v`: standard Tiny Tapeout wrapper and counter.
- `info.yaml`: submission metadata, source list, and pin descriptions.
- `docs/info.md`: placeholder datasheet describing the counter accurately.
- `test/`: Cocotb tests for RTL and the hardened gate-level netlist.
- `.github/workflows/`: RTL tests, datasheet generation, GDS build, precheck,
  gate-level tests, and layout viewer deployment, using the official TTSKY26d actions.

Run the simulation locally (requires Python 3.11+ and Icarus Verilog):

```sh
python3 -m venv .venv
.venv/bin/pip install -r test/requirements.txt
export PATH="$PWD/.venv/bin:$PATH"
make -C test
python -m cocotb_tools.check_results test/results.xml
```

The GDS workflow explicitly selects the pinned LibreLane version rather than
the action's moving default. The action manages its CI PDK installation; local
PDK pins remain in `flow/toolchain.env`. The workflows follow the
[official SKY130 template](https://github.com/TinyTapeout/ttsky-verilog-template).

After pushing, inspect the GitHub Actions results, particularly GDS, precheck,
and gate-level tests. In repository Settings → Pages, choose **GitHub Actions**
as the build source to enable the layout viewer. Once the build is green, we can
create the project together at [Tiny Tapeout](https://app.tinytapeout.com/),
select **TTSKY26d**, and connect this repository. No website submission has been
made yet. The counter metadata and documentation must be updated when the CPU
replaces the MVP.
