import scipy.signal as sig
import scipy.io as io
import numpy as np
import matplotlib.pyplot as plt

rate, data = io.wavfile.read('blackbird.wav')

left  = data[:, 0]
right = data[:, 1]

l = sig.lfilter([20, 1], [20], left)
r = sig.lfilter([20, 1], [20], right)

l = np.float32(l)
r = np.float32(r)

packed = np.array([l, r]).T



io.wavfile.write("filter_blackbird.wav", rate, packed)
print("done")