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

d = un.ufloat(50, 1)/1000 #m

plate_drag = un.ufloat(47.3, 0.05)/1000 * g
sphere_drag = un.ufloat(18.5, 0.05)/1000 * g
drop_drag = un.ufloat(6.6, 0.05)/1000 * g

plate_c_w = 8*plate_drag/(np.pi*d**2*v**2*rho)
sphere_c_w = 8*sphere_drag/(np.pi*d**2*v**2*rho)
drop_c_w = 8*drop_drag/(np.pi*d**2*v**2*rho)

print(f"{plate_c_w = }")
print(f"{sphere_c_w = }")
print(f"{drop_c_w = }")