from scipy.constants import g # typical earth gravity
from numpy import sqrt # utility
from uncertainties import unumpy as unp # uncertainty calculations
import matplotlib.pyplot as plt  # plotting

m = unp.uarray([
    327, 328, 329, 330, 331, 332, 333, 334, 334.5, 335, 335.5, 
    336, 336.5, 337, 337.5, 338, 338.5, 339, 340, 341, 342
    ], 0.25)/1000 # kg

# gravitational force from the weights * lever coefficient
Z = m * g * 2 # N
Z_s = unp.sqrt(Z) # sqrt(N)

A = unp.uarray([
    0.012, 0.016, 0.019, 0.021, 0.023, 0.026, 0.030, 
    0.048, 0.055, 0.063, 0.082, 0.110, 0.130, 0.161, 
    0.156, 0.112, 0.071, 0.052, 0.038, 0.031, 0.026
    ], sqrt(0.0005**2 + 0.0005**2))/2 # mm

# Adding text to the plot
plt.ylabel("A [mm]")
plt.xlabel("$\sqrt{Z}$ [$\sqrt{N}$]")
plt.title("Resonance plot")

# plotting the values with x and y error bars
plt.errorbar(unp.nominal_values(Z_s), unp.nominal_values(A), 
             unp.std_devs(A), unp.std_devs(Z_s), 
             fmt="o", capsize=3, capthick=0.75, 
             elinewidth=0.5, ms=1.5)
plt.savefig("uerrorbars_resonance.png", dpi=750)