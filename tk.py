import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import dot
from numpy.linalg import norm

y, sr=librosa.load('siren.wav')

print(y)
print(len(y))
print('sampling rate(HZ): %d', sr)
print('Audio length(seconds): %.2f' %(len(y)/sr))

tempo , _ = librosa.beat.beat_track(y,sr=sr)     
print(tempo)

zero_crossings = librosa.zero_crossings(y, pad=False)

print(zero_crossings)
print(sum(zero_crossings))

n0 = 0
n1 = len(y)

plt.figure(figsize=(16,6))
plt.plot(y[n0:n1])
plt.grid()
plt.show()


