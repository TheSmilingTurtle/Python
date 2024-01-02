import scipy.signal as sig
import numpy as np
import matplotlib.pyplot as plt

N = 10

tf = sig.dlti([1,0],np.polymul([1,-0.2],[1,-0.5]))
t, (resp,) = tf.impulse(n=N)

x = np.linspace(0,N,1000)
a = 3/10*(0.5**x + 0.2**x)
b = 10/3*(-0.5**x+0.2**x)
c = 10/3*(0.5**x - 0.2**x)
d = 3/10*(0.5**x-0.2**(-x))

plt.plot(x,a, label="A")
plt.plot(x,b, label="B")
plt.plot(x,c, label="C")
#plt.plot(x,d, label="D")
plt.step(t, resp.flatten(), label="System")
plt.legend()
plt.show()