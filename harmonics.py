import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import sph_harm

def spherical_harmonics(n, l, ml, ms):
    theta, phi = np.mgrid[0:np.pi:200j, 0:2*np.pi:200j] 
    r = np.abs(sph_harm(ml, l, phi, theta))**2
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)

    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis', edgecolor='none', alpha=0.8)

    ax.view_init(elev=30, azim=30)
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    
    ax.set_box_aspect([1, 1, 1])
    plt.title(f'Spherical Harmonic for n={n}, l={l}, ml={ml}, ms={ms}', fontsize=16)
    plt.colorbar(surf, shrink=0.5, aspect=5)
    plt.savefig(f'spherical_harmonic_n{n}_l{l}_ml{ml}_ms{ms}.png', bbox_inches='tight')

n = int(input("Enter principal quantum number (n): "))
l = int(input("Enter angular momentum quantum number (l): "))
ml = int(input("Enter magnetic quantum number (ml): "))
ms = float(input("Enter spin quantum number (ms): "))
spherical_harmonics(n, l, ml, ms)
