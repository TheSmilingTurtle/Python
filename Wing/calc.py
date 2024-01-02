import uncertainties as un
from uncertainties.umath import sqrt

p1 = un.ufloat(20, 5)
p2 = un.ufloat(240, 5)
rho = 1.2 #of air

print(p2 - p1)

v = sqrt(2*(p2-p1)/rho)

print(v)