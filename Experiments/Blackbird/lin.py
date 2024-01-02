import scipy.signal as sig
import scipy.io as io
import numpy as np
import matplotlib.pyplot as plt

rate, data = io.wavfile.read('blackbird.wav')

left  = data[:, 0]
right = data[:, 1]

lowpass_filter = sig.butter(1, 2800, "high", fs=rate)
lconv = sig.lfilter(*lowpass_filter, left)
rconv = sig.lfilter(*lowpass_filter, right)

# lcorr = sig.correlate(lconv, lconv, "same")
# rcorr = sig.correlate(rconv, rconv, "same")

l = np.float32(lconv)
r = np.float32(rconv)

packed = np.array([l, r]).T

io.wavfile.write("lin.wav", rate, packed)
print("done")

freqs = np.linspace(0,1,1000)
w, mag, phase = sig.bode(lowpass_filter, freqs)
plt.figure()
plt.semilogx(w*rate, mag)    # Bode magnitude plot
plt.figure()
plt.semilogx(w*rate, phase)  # Bode phase plot
plt.show()
