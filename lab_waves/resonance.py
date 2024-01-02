from scipy.constants import g
import numpy as np 
import matplotlib.pyplot as plt

m = np.array([
    327, 328, 329, 330, 331, 332, 333, 334, 334.5, 335, 335.5, 
    336, 336.5, 337, 337.5, 338, 338.5, 339, 340, 341, 342
])

Z = 2 * m/1000 * g

A = np.array([
    0.012, 0.016, 0.019, 0.021, 0.023, 0.026, 0.030, 0.048, 0.055, 0.063, 0.082, 
    0.11, 0.13, 0.161, 0.156, 0.112, 0.071, 0.052, 0.038, 0.031, 0.026
])

plt.ylabel("A [mm]")
plt.xlabel("$\sqrt{Z}$ [$\sqrt{N}$]")

plt.title("Resonance plot")
plt.scatter(np.sqrt(Z), A)
plt.show()