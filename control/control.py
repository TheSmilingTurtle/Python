import scipy.signal as sig
import numpy as np 
import matplotlib.pyplot as plt 

p = (-2, -1)
z = (-0.15, -0.8, -0.2)
g = 1

kp = 0
kd = -1
ki = 0

den = [1, 0]
num = [kd, kp, ki]

sys = sig.TransferFunction(sig.lti(p,z,g))
print(sys)
cont = sig.lti(num, den)
print(cont)

total = sig.lti(np.polymul(sys.num, cont.num), np.polymul(sys.den, cont.den))
print(total)


#rg, mag, phase = sig.bode(total, n=1000)

#phase = np.deg2rad(phase)

#fig, (ax1, ax2) = plt.subplots(2)
#ax1.loglog(rg, mag)
#ax2.plot(rg, phase)
#ax2.set_xscale("log")

t = np.linspace(0,100,1000)
t, resp = total.step(T=t)

fig, ax = plt.subplots(1)
ax.plot(t, resp)

plt.show()