import scipy.signal as sig
import scipy.io as io
import numpy as np
import matplotlib.pyplot as plt

rate, data = io.wavfile.read('blackbird.wav')

left  = data[:, 0]
right = data[:, 1]
print("extracted data")

lfft = np.fft.fft(left)
rfft = np.fft.fft(right)
print("computed fft")

lnoise = np.random.standard_normal(lfft.size)
rnoise = np.random.standard_normal(rfft.size)

lf = lfft + lnoise
rf = rfft + rnoise
print("computed filter")

ilf = np.abs(np.fft.ifft(lf))
irf = np.abs(np.fft.ifft(rf))
print("computed ifft")

min_val = np.min(ilf)
max_val = np.max(ilf)
ilf = 2 * (ilf - min_val) / (max_val - min_val) - 1

min_val = np.min(irf)
max_val = np.max(irf)
irf = 2 * (irf - min_val) / (max_val - min_val) - 1

ilf = np.float32(ilf)
irf = np.float32(irf)

packed = np.array([ilf, irf]).T

io.wavfile.write("noise_blackbird.wav", rate, packed)
print("done")

fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(list(range(len(lf))), np.abs(lf))
ax2.plot(list(range(len(rf))), np.abs(rf))
plt.show()