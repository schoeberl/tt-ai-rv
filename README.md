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
