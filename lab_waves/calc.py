import numpy as np
from scipy.constants import g 

l = np.arange(36, 52, 2)/100 # +-0.01 m

m = np.array([
    275, 305, 338, 374.5, 411, 450, 490, 534.5
])/1000 # +-0.0025 kg

Z = m * g * 2
Z_err = 0.0025 * g * 2

print(f"{Z_err=}")

mu = 7.06e-4 #kg/m

n = 1/(2 * l) * np.sqrt(Z/mu)
n_err =  n * np.sqrt( ( 0.01 / (2 * l) )**2 + (0.5 * Z_err / Z)**2 )

print(n)
print(n_err)

print("mean:", n.mean(), "+-", np.linalg.norm(n_err))