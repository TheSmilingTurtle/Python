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
ltruncfft = lfft*np.sin(np.linspace(1, 10, lfft.size))
rtruncfft = rfft*np.cos(np.linspace(1, 10, rfft.size))
print("truncating fft")
ltrunc = np.abs(np.fft.ifft(ltruncfft))
rtrunc = np.abs(np.fft.ifft(rtruncfft))
print("computed ifft")
min_val = np.min(ltrunc)
max_val = np.max(ltrunc)
ltrunc = 2 * (ltrunc - min_val) / (max_val - min_val) - 1

min_val = np.min(rtrunc)
max_val = np.max(rtrunc)
rtrunc = 2 * (rtrunc - min_val) / (max_val - min_val) - 1

ltrunc = np.float32(ltrunc)
rtrunc = np.float32(rtrunc)
print("computed normalization")

packed = np.array([ltrunc, rtrunc]).T

io.wavfile.write("trunc_blackbird.wav", rate, packed)
print("done")