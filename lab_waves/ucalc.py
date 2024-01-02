from scipy.constants import g # typical earth gravity
from uncertainties import unumpy as unp # uncertainty calculations

l = unp.uarray(range(36, 52, 2), 1)/100 # m

m = unp.uarray(
    [275, 305, 338, 374.5, 411, 450, 490, 534.5]
    , 0.25)/1000 # kg

# gravitational force from the weights * lever coefficient
Z = m * g * 2 #N

mu = 7.06e-4 # kg/m

# from the formula for nu1
n = 1/(2 * l) * unp.sqrt(Z/mu)

n_mean = n.mean() #the mean that we recieve
print(f"\n{n_mean = }")