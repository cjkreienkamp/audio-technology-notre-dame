import librosa
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

file_path = 'file_example_WAV_1MG.wav'
samples , sampling_rate = librosa.load(file_path, sr = None, mono = True, offset = 0.0, duration = None)

plt.figure()
#plt.stem(x,y3, 'r', use_line_collection = True )
plt.plot(samples)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
# plt.show()

import scipy
def fft_plot(audio, sampling_rate):
    n = len(audio)
    T = 1/sampling_rate
    yf = scipy.fft.fft(audio)
    xf = np.linspace(0.0, 1.0/(2.0*T), n//2)
    fig, ax = plt.subplots()
    ax.plot(xf, 2.0/n * np.abs(yf[:n//2]))
    plt.grid()
    plt.xlabel('Frequency')
    plt.ylabel('Magnitude')
    return plt.show()

fft_plot(samples,sampling_rate)
