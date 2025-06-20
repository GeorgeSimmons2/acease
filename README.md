# ACEASE

[ASE](https://wiki.fysik.dtu.dk/ase/) calculator for ACE models. Compatible with [ACEpotentials.jl](https://github.com/ACEsuit/ACEpotentials.jl) version 0.8.2.

## Installation

Before installing, make sure Julia is installed (it can be installed by following the instructions [here](https://julialang.org/downloads/platform/)).

The packages within Julia can be installed using the following command:
```julia
] add AtomsCalculators@0.2.2 AtomsCalculatorsUtilities@0.1.5 AtomsBase@0.4.2 Unitful@1.21.0 PythonCall@0.9.22 https://github.com/wgst/NQCBase.jl.git 
```

To install this calculator, follow the instructions below:
```sh
git clone https://github.com/wgst/acease.git
cd acease
pip install .
python -c "import julia; julia.install()"
```

To use specific Julia environment, use this command before running the script:
'''sh
export JULIA_PROJECT=/path/to/julia/environment
'''