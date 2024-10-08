import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import sph_harm

def spherical_harmonics(n, l, ml, ms):
    theta, phi = np.mgrid[0:np.pi:100j, 0:2*np.pi:100j]
    r = np.abs(sph_harm(ml, l, phi, theta))**2
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, rstride=1, cstride=1, color='c', edgecolor='k', alpha=0.6)
    ax.set_xlim([-0.5, 0.5])
    ax.set_ylim([-0.5, 0.5])
    ax.set_zlim([-0.5, 0.5])
    ax.set_box_aspect([1, 1, 1])
    plt.title(f'Plot for Reaction {n}')
    plt.savefig(f'spherical_harmonic_n{n}_l{l}_ml{ml}_ms{ms}.png')

n = int(input("Enter principal quantum number (n): "))
l = int(input("Enter angular momentum quantum number (l): "))
ml = int(input("Enter magnetic quantum number (ml): "))
ms = float(input("Enter spin quantum number (ms): "))
spherical_harmonics(n, l, ml, ms)
