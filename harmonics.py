import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.special import sph_harm

def plot_spherical_harmonic(l, ml):
    phi = np.linspace(0, 2 * np.pi, 100)
    theta = np.linspace(0, np.pi, 100)
    phi, theta = np.meshgrid(phi, theta)
    
    # Calculate the spherical harmonic
    Y_lm = sph_harm(ml, l, phi, theta)
    
    # Calculate the spherical coordinates
    r = np.abs(Y_lm)
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    
    # Plotting the surface
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    mappable = ax.plot_surface(x, y, z, facecolors=plt.cm.viridis(r), rstride=1, cstride=1, antialiased=True)
    
    # Add colorbar
    plt.colorbar(mappable, shrink=0.5, aspect=20, label='|Y_lm| (normalized)')
    
    # Save the plot as a PNG file
    filename = f'spherical_harmonic_l{l}_ml{ml}.png'
    plt.savefig(filename, dpi=300)
    print(f"Plot saved as {filename}")

def main():
    l = int(input("Enter angular momentum quantum number (l): "))
    ml = int(input(f"Enter magnetic quantum number (ml) (|ml| <= {l}): "))
    plot_spherical_harmonic(l, ml)

if __name__ == "__main__":
    main()
