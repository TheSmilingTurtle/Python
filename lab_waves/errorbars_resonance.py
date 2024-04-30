from scipy.constants import g
import numpy as np
import matplotlib.pyplot as plt

m = np.array([
    327, 328, 329, 330, 331, 332, 333, 334, 334.5, 335, 335.5, 
    336, 336.5, 337, 337.5, 338, 338.5, 339, 340, 341, 342
    ])/1000 #  +-0.25
m_err = 0.00025

Z = 2 * m * g
Z_err = 2 * m_err * g

Z_s = np.sqrt(Z)
Z_s_err = Z_s * 0.5 * Z_err / Z

A = np.array([
    0.012, 0.016, 0.019, 0.021, 0.023, 0.026, 0.030, 0.048, 0.055, 0.063, 0.082, 
    0.11, 0.13, 0.161, 0.156, 0.112, 0.071, 0.052, 0.038, 0.031, 0.026
    ])/2
A_err = np.sqrt(0.0005**2 + 0.0005**2)/2

print(m)
print(Z)
print(Z_s)
print(A)

plt.ylabel("A [mm]")
plt.xlabel("$\sqrt{Z}$ [$\sqrt{N}$]")

plt.title("Resonance plot")
plt.errorbar(Z_s, A, A_err, Z_s_err, fmt="o", capsize=3, elinewidth=0.5, ms=1.5)
plt.show()