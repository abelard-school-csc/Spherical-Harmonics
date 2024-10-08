# Spherical Harmonics 3D Renderer

## Overview

This project provides a Python-based tool for generating 3D visualizations of spherical harmonics. Spherical harmonics are a set of special functions defined on the surface of a sphere, often used in quantum mechanics, geophysics, and computer graphics. They depend on quantum numbers `n`, `l`, `m`, and their corresponding quantum states. The program renders the spherical harmonics and exports them as PNG images.

## Spherical Harmonics

Spherical harmonics are functions that arise when solving the angular part of Laplace's equation in spherical coordinates. They are used to describe the angular dependence of solutions to Schrödinger's equation for atoms, among other things. Given quantum numbers `l` and `m`, the spherical harmonics are defined as:

$$Y_l^m(\theta, \phi)$$

Where:
- `l` is the angular momentum quantum number.
- `m` is the magnetic quantum number.
- `\theta` and `\phi` are the polar and azimuthal angles, respectively.

These functions play a key role in fields like quantum mechanics, where they describe electron orbitals, and in 3D graphics, where they approximate complex functions over a sphere.

## How the Program Works

1. The user specifies quantum numbers `n`, `l`, and `m`.
2. The program calculates the spherical harmonics using `scipy.special.sph_harm`.
3. A 3D plot is generated using `matplotlib` based on the magnitude of the spherical harmonics.
4. The 3D plot is saved as a PNG image.

### Example Usage

To generate a 3D plot of the spherical harmonic with `n=3`, `l=2`, and `m=1`, you can run the following code:

```bash
python3 harmonics.py
```

This will save a PNG file named `spherical_harmonic_n3_l2_m1.png`.

## Installation Instructions

### Prerequisites

1. Python 3.x
2. `matplotlib` for 3D plotting
3. `scipy` for calculating spherical harmonics
4. `numpy` for array manipulations

### Cloning the Repository

You can clone the repository with the following command:

```bash
git clone https://github.com/abelard-school-csc/Spherical-Harmonics.git
cd Spherical-Harmonics
```

### Installing the Requirements

To install the necessary Python dependencies, run:

```bash
pip install -r requirements.txt
```

### Requirements

```text
numpy
matplotlib
scipy
```

## License

This project is licensed under the MIT License.
