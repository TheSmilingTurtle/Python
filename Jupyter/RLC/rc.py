import numpy as np
import uncertainties as un 
import uncertainties.unumpy as unp
import matplotlib.pyplot as plt

R = un.ufloat(1000, 10)

f = unp.uarray([10.045, 101.155, 301, 515, 1020, 1595, 10060, 14800, 35100, 103600], [0.005, 0.04, 0.5, 0.5, 1, 8, 10, 100, 100, 1000])
w = 2 * np.pi * f
U_in = unp.uarray([1.02, 1.02, 1.04, 1.02, 1, 1, 1, 1.02, 1.02, 1], 0)
U_out = unp.uarray([1.02, 1.02, 1.04, 0.96, 0.84, 0.7, 0.18, 0.14, 0.057, 0.026], [0, 0, 0, 0, 0, 0, 0, 0, 0.004, 0.002])
ratio = U_out/U_in
I_r = (U_out - U_in) / R
phase_shift = unp.uarray([0, -4, -10.4, -18.5, -32, -45, -76, -82, -87, -92.6], [0, 0.5, 1, 1, 1, 0.5, 5, 5, 3, 8])

I_r_phase_freq = unp.uarray([161.5, 1600, 17740], [0.3, 8, 40])
I_r_phase_shift = unp.uarray([100, 90.5, 88.2], [5, 1, 2])

fig, ax = plt.subplots()
ax.errorbar(unp.nominal_values(w), unp.nominal_values(ratio), unp.std_devs(ratio), unp.std_devs(w), label="Tansfer function", capsize=3)
ax.hlines(0.7, min(w).nominal_value, max(w).nominal_value, color="orange", label="0.7")
ax.vlines(1e4, 0, 1, color="green", linestyle="dashed", label="$10^4 [rad/s]$")
ax.set_xscale("log")
ax.set_xlabel("Angular frequency [rad/s]")
ax.set_ylabel("$U_{out}/U_{in}$ $[1]$")
ax.set_title("Transfer function of the RC cirquit")
ax.legend()
fig.savefig("Ratio_RC.png")

# fig, ax = plt.subplots()
# ax.errorbar(unp.nominal_values(w), unp.nominal_values(phase_shift), unp.std_devs(phase_shift), unp.std_devs(w), label="Phase shift", capsize=3)
# ax.hlines(-45, min(w).nominal_value, max(w).nominal_value, color="orange", label="$-45\\degree$")
# ax.vlines(1e4, min(phase_shift).nominal_value, max(phase_shift).nominal_value, color="green", linestyle="dashed", label="$10^4$ $[rad/s]$")
# ax.set_xscale("log")
# ax.set_xlabel("Angular frequency [rad/s]")
# ax.set_ylabel("Phase shift [deg]")
# ax.set_title("Phase shift of the RC cirquit")
# ax.legend()
# fig.savefig("Phase_Shift_RC.png")