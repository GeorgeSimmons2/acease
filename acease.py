import numpy as np
from ase.calculators.calculator import Calculator
from ase.constraints import voigt_6_to_full_3x3_stress, full_3x3_to_voigt_6_stress

from julia.api import Julia
jl = Julia(compiled_modules=False)

from julia import Main

Main.eval("ENV[\"JULIA_CONDAPKG_BACKEND\"] = \"Null\"")
Main.eval("ENV[\"JULIA_PYTHONCALL_EXE\"] = \"/gpfs/home/m/msrmnk2/mace-mp/bin/python\"")

Main.eval("using PythonCall")
Main.eval("using ASEconvert")
Main.eval("using AtomsCalculators")
Main.eval("using AtomsBase")
Main.eval("using Unitful")

from julia.AtomsCalculators import potential_energy, forces, virial

pyconv = Main.eval("pyconv(a) = ASEconvert.ase_to_system(a)")
py = Main.eval("py(a) = PythonCall.Py(a)")
ustrip = Main.eval("ustrip(a) = Unitful.ustrip.(a)")




def ACEpotentials(potname):
    Main.eval("using ACEpotentials: load_model")
    Main.eval("ace_model, ace_model_meta = load_model(\"" + potname + "\")")

    model = ACEpotentialsCalculator("ace_model")
    return model


class ACEpotentialsCalculator(Calculator):
    """
    ASE-compatible Calculator that calls AtomsCalculators.jl for forces and energy
    """
    implemented_properties = ['forces', 'energy', 'free_energy', 'stress']
    default_parameters = {}
    name = 'ACECalculator'

    def __init__(self, ace_calculator):
        Calculator.__init__(self)
        self.ace_calculator = Main.eval(ace_calculator) #julia.eval

    def calculate(self, atoms, properties, system_changes):
        Calculator.calculate(self, atoms, properties, system_changes)
        system = pyconv(atoms)
        self.results = {}
        if 'energy' in properties:
            E = ustrip(potential_energy(system, self.ace_calculator))
            self.results['energy'] = E
            self.results['free_energy'] = E
        if 'forces' in properties:
            F = ustrip(forces(system, self.ace_calculator))
            self.results['forces'] = F
        if 'stress' in properties:
            volume = atoms.get_volume()
            voigt_stress = -full_3x3_to_voigt_6_stress(ustrip(virial(system, self.ace_calculator)))/volume
            self.results['stress'] = voigt_stress
            
