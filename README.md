# ACEASE

[ASE](https://wiki.fysik.dtu.dk/ase/) calculator for ACE models. Compatible with [ACEpotentials.jl](https://github.com/ACEsuit/ACEpotentials.jl) version 0.8.2.

## Installation

Before installing, make sure Julia and the following Julia packages are installed:
```
ACEpotentials
PythonCall
ASEconvert
AtomsCalculators
AtomsBase
Unitful
```
Julia can be installed by following the instructions [here](https://julialang.org/downloads/platform/).

The packages within Julia can be installed using the following commands:
```julia
using Pkg
Pkg.add(url="https://github.com/ACEsuit/ACEpotentials.jl.git", rev="43ae686")
Pkg.add(["PythonCall", "ASEconvert", "AtomsCalculators", "AtomsBase", "Unitful"])
```


To install this calculator, follow the instructions below:
```sh
git clone https://github.com/wgst/acease.git
cd acease
pip install .
```
