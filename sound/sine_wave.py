#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyaudio
import numpy as np
from scipy.io.wavfile import write

p = pyaudio.PyAudio()

f = 440.0  # sine frequency, Hz, may be float
sr = 44100  # sampling rate, Hz, must be integer
volume = 1.0  # range [0.0, 1.0]
duration = 5.0 # in seconds, may be float

# generate samples, note conversion to float32 array
time_dots = np.arange(sr * duration) / sr
samples = (np.sin(2 * np.pi * f * time_dots)).astype(np.float32)

# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
       channels=1,
       rate=sr,
       output=True)

# play. May repeat with different volume values (if done interactively)
stream.write(volume * samples)

stream.stop_stream()
stream.close()

p.terminate()

sound = np.int16(samples * 32767)
write("test.wav", sr, sound)
