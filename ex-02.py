import librosa
import matplotlib

file_path = 'file_example_WAV_1MG.wav'
samples , sampling_rate = librosa.load(file_path, sr = None, mono = True, offset = 0.0, duration = None)

from librosa import display
from matplotlib import pyplot as plt
plt.figure()
librosa.display.waveplot(y = samples, sr = sampling_rate)
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.show()
