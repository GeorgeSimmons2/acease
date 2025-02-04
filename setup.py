from setuptools import setup, find_packages

setup(
    name="acease",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "ase",
        "julia",
    ],
    python_requires=">=3.7",
)