import matplotlib.pyplot as plt 
import numpy as np
from scipy.constants import g

l = np.arange(36, 52, 2)/100

m = np.array([
    275, 305, 338, 374.5, 411, 450, 490, 534.5
]) # +-0.25

Z = m/1000 * g * 2

plt.xlabel("$l^2$  [cm$^2$]")
plt.ylabel("Z [N]")
plt.title("Force at resonance")

plt.scatter(l**2, Z)
plt.show()