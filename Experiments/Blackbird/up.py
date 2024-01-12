import scipy.signal as sig
import scipy.io as io
import numpy as np
import matplotlib.pyplot as plt

def upconverter(L, Omega_c):
    '''
    INPUT
        L: integer, length of the audio signal
        Omega_c: float, discrete frequency of the discrete-time carrier signal
    OUTPUT
        up: the upconverted audio signal
    '''
    # a bunch of things cancel and you get a kinda nice looking form
    return np.real(np.exp(1j*Omega_c*np.arange(0, L)))

def downconverter(L, Omega_c):
    '''
    INPUT
        L: integer, length of the audio signal
        Omega_c: float, discrete frequency of the discrete-time carrier signal
    OUTPUT
        up: the upconverted audio signal
    '''
    # a bunch of things cancel and you get a kinda nice looking form
    return np.real(np.exp(-1j*Omega_c*np.arange(0, L)))

rate, data = io.wavfile.read('blackbird.wav')

left  = data[:, 0]
right = data[:, 1]

fc = 10000
Omega_c = 2 * np.pi * fc / rate

l = left * upconverter(len(left), Omega_c)
r = right * upconverter(len(right), Omega_c)
l = l * downconverter(len(l), Omega_c)
r = r * downconverter(len(r), Omega_c)

numtaps = 101
a = sig.firwin(numtaps, fc/2, fs=rate)
l = sig.convolve(a, l)
r = sig.convolve(a, r)

min_val = np.min(l)
max_val = np.max(l)
ltrunc = 2 * (l - min_val) / (max_val - min_val) - 1

min_val = np.min(r)
max_val = np.max(r)
rtrunc = 2 * (r - min_val) / (max_val - min_val) - 1

lout = np.float32(ltrunc)
rout = np.float32(rtrunc)
print("computed normalization")

packed = np.array([lout, rout]).T


io.wavfile.write("upshifted_blackbird.wav", rate, packed)
print("done")