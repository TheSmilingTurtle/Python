import scipy.signal as sig
import scipy.io as io
import numpy as np
import matplotlib.pyplot as plt

rate, data = io.wavfile.read('blackbird.wav')

left  = data[:, 0]
right = data[:, 1]

l = np.clip(left, 0, 1)
r = np.clip(right, 0, 1)

l = np.float32(l)
r = np.float32(r)

packed = np.array([l, r]).T

plt.plot(list(range(1000)), l[10000:11000])
plt.show()

io.wavfile.write("climp_blackbird.wav", rate, packed)
print("done")