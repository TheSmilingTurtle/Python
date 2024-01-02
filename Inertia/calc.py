from uncertainties import ufloat, umath
from uncertainties import unumpy as unp
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt 


empty_times = np.array([
    6.27, 6.63, 6.44
])

empty_times_mean = ufloat(empty_times.mean(), st.sem(empty_times))
print(empty_times_mean)

mass = ufloat(3.080, 0.0005) # kg
radius = ufloat(23.7, 0.05)/200 # m

disc_inertia = mass * radius**2 / 2 # kg*m^2
print(disc_inertia)

disc_times = np.array([
    8.27, 8.19, 8.15
])

disc_times_mean = ufloat(disc_times.mean(), st.sem(disc_times))
print(disc_times_mean)

D = 4 * np.pi**2 * disc_inertia / (disc_times_mean**2 - empty_times_mean**2) # kg*m^2/s^2
print(D)

bar_mass_1 = ufloat(0.611, 0.0005) # kg
bar_mass_2 = ufloat(0.605, 0.0005) # kg

bar_times_1 = np.array([
    6.71, 6.91, 6.75
])
bar_times_mean_1 = ufloat(bar_times_1.mean(), st.sem(bar_times_1))

bar_times_2 = np.array([
    7.39, 7.5, 7.41
])
bar_times_mean_2 = ufloat(bar_times_2.mean(), st.sem(bar_times_2))

bar_times_3 = np.array([
    8.3, 8.59, 8.53
])
bar_times_mean_3 = ufloat(bar_times_3.mean(), st.sem(bar_times_3))

bar_times_4 = np.array([
    9.83, 9.78, 9.66
])
bar_times_mean_4 = ufloat(bar_times_4.mean(), st.sem(bar_times_4))

bar_times_5 = np.array([
    11.27, 11.25, 11.37
])
bar_times_mean_5 = ufloat(bar_times_5.mean(), st.sem(bar_times_5))

bar_times = np.array([empty_times_mean, bar_times_mean_1, bar_times_mean_2, bar_times_mean_3, bar_times_mean_4, bar_times_mean_5])

thetas = D * bar_times**2 / (4 * np.pi**2)

steiner = []

for r in range(0, 30, 5):
    steiner.append((bar_mass_1 + bar_mass_2)*(r/100)**2)
steiner_calculated = np.array(steiner)

steiner_experimental = thetas - thetas[0]

print(steiner_experimental)
print(steiner_calculated)
print(steiner_experimental - steiner_calculated)

plt.title("Theroetical vs Experimental steiner Term")
plt.xlabel("$r^2$")
plt.ylabel("$\\theta_s$")

plt.plot(np.arange(0, len(thetas)*5, 5)**2, unp.nominal_values(steiner_calculated), label="Theretical Steiner Term")
plt.errorbar(np.arange(0, len(thetas)*5, 5)**2, unp.nominal_values(steiner_experimental), unp.std_devs(steiner_experimental), elinewidth=1, linewidth=0, capsize=2, label="Experiments Steiner Term")

plt.legend()

plt.savefig("steiner.png")

print()

print(empty_times_mean)
print(bar_times_mean_1)
print(bar_times_mean_2)
print(bar_times_mean_3)
print(bar_times_mean_4)
print(bar_times_mean_5)
