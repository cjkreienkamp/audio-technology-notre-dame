import librosa

file_path = 'file_example_WAV_1MG.wav'
samples , sampling_rate = librosa.load(file_path, sr = None, mono = True, offset = 0.0, duration = None)
duration_of_sound = len(samples) / sampling_rate
print('sampling rate:',sampling_rate)
print(duration_of_sound,'seconds')
