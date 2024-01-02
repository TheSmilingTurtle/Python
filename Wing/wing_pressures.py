import uncertainties as un
from uncertainties.umath import sqrt
from uncertainties import unumpy as unp
import matplotlib.pyplot as plt
from scipy.integrate import simpson
import numpy as np

p1 = un.ufloat(20, 5)
p2 = un.ufloat(240, 5)
rho = 1.2 #of air

v = sqrt(2*(p2-p1)/rho)

zero_angle = unp.uarray([240, -80, -100, -60, -30, -150, -30, -20, -10], 5)
ten_angle = unp.uarray([200, -170, -110, -50, -20, -30, -10, -10, -10], 5)

top_points = np.array([0, 9, 38, 66, 99])/1000 #m
bottom_points = np.array([0, 10, 35, 80, 115])/1000 #m

zero_upside = zero_angle[:5] 
zero_underside = np.hstack([zero_angle[0], zero_angle[5:]])

ten_upside = ten_angle[:5] 
ten_underside = np.hstack([ten_angle[0], ten_angle[5:]])

zero_top_int = simpson(zero_upside, top_points)
zero_bottom_int = simpson(zero_underside, bottom_points)

ten_top_int = simpson(ten_upside, top_points)
ten_bottom_int = simpson(ten_underside, bottom_points)

zero_A = zero_bottom_int-zero_top_int
ten_A = ten_bottom_int-ten_top_int

zero_G = zero_A/(rho*v)
ten_G = ten_A/(rho*v)

print(v)
print(zero_A)
print(zero_G)
print()
print(ten_A)
print(ten_G)

fig, ax = plt.subplots()
ax.errorbar(top_points, unp.nominal_values(zero_upside), unp.std_devs(zero_upside), capsize=5, label="Top side")
ax.errorbar(bottom_points, unp.nominal_values(zero_underside), unp.std_devs(zero_underside), capsize=5, label="Bottom side")
ax.set_title("Pressures on the two sides of the wing at $\\alpha = 0\degree$")
ax.set_ylabel("Pressure in [Pa]")
ax.set_xlabel("Position on the wing [m]")
ax.legend()
plt.savefig("Zero_pressures.png")