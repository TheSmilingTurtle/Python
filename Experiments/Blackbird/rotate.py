import scipy.signal as sig
import scipy.io as io
import numpy as np
import matplotlib.pyplot as plt

rate, data = io.wavfile.read('blackbird.wav')

left  = data[:, 0]
right = data[:, 1]

s = np.square(np.sin(np.linspace(0, 8*np.pi, left.size)))
c = np.square(np.cos(np.linspace(0, 8*np.pi, right.size)))

l = left * s
r = right * c

l = np.float32(l)
r = np.float32(r)

packed = np.array([l, r]).T

io.wavfile.write("rot_blackbird.wav", rate, packed)
print("done")