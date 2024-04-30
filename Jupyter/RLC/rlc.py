import numpy as np
import uncertainties as un 
from uncertainties.umath import sqrt
import uncertainties.unumpy as unp
import matplotlib.pyplot as plt

R = un.ufloat(1000, 10)
L = un.ufloat(10e-3, 0)
C = un.ufloat(100e-9, 0)
theoretical_resonance = 1 / (sqrt(L * C) * 2 * np.pi)
Q = R * sqrt(C/L)

print(Q)

f = unp.uarray([3235, 4075, 4470, 5012, 5260, 5530, 6000, 7065, 8010], [15, 20, 15, 20, 20, 20, 15, 30, 20])
w = 2 * np.pi * f
U_in = unp.uarray([1.38, 1.38, 1.4, 1.42, 1.42, 1.42, 1.4, 1.38, 1.38], 0)
U_out = unp.uarray([0.373, 0.67, 0.88, 1.2, 1.24, 1.18, 0.96, 0.6, 0.45], [0.003, 0.01, 0, 0, 0, 0, 0, 0, 0.01])
ratio = U_out/U_in
phase_shift = unp.uarray([70, 56, 42, 13.5, -1.5, -17.7, -39, -60.3, -65], [1.5, 2, 2, 0.5, 1, 0.7, 1, 1, 4])

# fig, ax = plt.subplots()
# ax.errorbar(unp.nominal_values(w), unp.nominal_values(phase_shift), unp.std_devs(phase_shift), unp.std_devs(w), label="Phase Shift", capsize=3)
# ax.hlines(0, min(w).nominal_value, max(w).nominal_value, color="orange", label="$0\degree$")
# ax.vlines(2 * np.pi * theoretical_resonance.nominal_value, min(phase_shift).nominal_value, max(phase_shift).nominal_value, color="green", linestyle="dashed", label="Theoretical Resonance")
# ax.set_xscale("log")
# ax.set_xlabel("Angular frequency [rad/s]")
# ax.set_ylabel("$Phase Shift [deg]$")
# ax.set_title("Phase shift of an RLC cirquit as a dependency of the angular frequency")
# ax.legend()
# fig.savefig("Phase_Shift_RLC.png")

fig, ax = plt.subplots()
ax.errorbar(unp.nominal_values(w), unp.nominal_values(ratio), unp.std_devs(ratio), unp.std_devs(w), label="Transfer function", capsize=3)
ax.hlines(0.7, min(w).nominal_value, max(w).nominal_value, color="orange", label="$0.7$")
ax.vlines(2 * np.pi * theoretical_resonance.nominal_value, 0, 1, color="green", linestyle="dashed", label="Theoretical Resonance")
ax.set_xscale("log")
ax.set_xlabel("Angular frequency [rad/s]")
ax.set_ylabel("$U_{out}/U_{in}$ $[1]$")
ax.set_title("Transfer function of the RLC cirquit")
ax.legend()
fig.savefig("Ratio_RLC.png")