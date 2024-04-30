from uncertainties import ufloat, umath
from uncertainties import unumpy as unp
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt 

times = unp.uarray([
    10.47, 10.53, 10.85, 11.41, 12.06, 12.75, 13.53, 13.93, 14.25, 14.47
], 0.1)/3 # s

phi = np.linspace(np.pi/2, 0, 10)

lin = np.cos(phi)**2

print(times)


x = [lin[0], lin[-1]]
y = [times[0].nominal_value, times[-1].nominal_value]

plt.title("Dumbell Tilt angle and period")
plt.xlabel("$cos^2(\\varphi)$")
plt.ylabel("T")

plt.plot(x,y, label="Linear Relation")
plt.errorbar(lin, unp.nominal_values(times), unp.std_devs(times), elinewidth=1, linewidth=0, capsize=2, label="Measured Period")

plt.legend()

plt.savefig("cos_linear.png")