from scipy.constants import g # typical earth gravity
from uncertainties import unumpy as unp # uncertainty calculations
import matplotlib.pyplot as plt # plotting

l = unp.uarray(range(36, 52, 2), 1) # cm

m = unp.uarray(
    [275, 305, 338, 374.5, 411, 450, 490, 534.5]
    , 0.25)/1000 # kg

# gravitational force from the weights * lever coefficient
Z = m * g * 2 # N

# Adding text to the plot
plt.xlabel("$l^2$  [cm$^2$]")
plt.ylabel("Z [N]")
plt.title("Force at resonance")

# plotting the values with x and y error bars
plt.errorbar(unp.nominal_values(l**2), unp.nominal_values(Z), 
             unp.std_devs(Z), unp.std_devs(l**2), 
             fmt="o", capsize=3, capthick=0.75, 
             elinewidth=0.5, ms=1.5)
plt.savefig("uerrorbars_force_at_resonance.png", dpi=750)