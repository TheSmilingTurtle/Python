import uncertainties as un
from uncertainties.umath import sqrt
from uncertainties import unumpy as unp
import matplotlib.pyplot as plt
from scipy.integrate import simpson
from scipy.constants import *
import numpy as np

p1 = un.ufloat(20, 5)
p2 = un.ufloat(240, 5)
rho = 1.2 #of air

v = sqrt(2*(p2-p1)/rho)

A = unp.uarray([1, 12, 24, 36, 46, 60, 70, 82], 1)/1000 * g #N
W = unp.uarray([16.8, 14.2, 13.1, 13.3, 14.3, 16.3, 18.5, 22.0], 1)/1000 * g #N
alpha = np.pi*np.arange(-9, 15, 3)/180

d = un.ufloat(100, 1)/1000 #m

W_pred = 2 * A**2/(np.pi*d**2*rho*v**2)

print(W_pred*1000/g)

fig, ax = plt.subplots()
ax.errorbar(unp.nominal_values(W), unp.nominal_values(A), unp.std_devs(A), unp.std_devs(W), capsize=5)
ax.set_title("Lilienthal's polar diagram")
ax.set_ylabel("Lift [N]")
ax.set_xlabel("Drag [N]")
plt.savefig("Lillenthal.png")