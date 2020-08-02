#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy.io.wavfile import write


f = 440.0  # sine frequency, Hz, may be float
sr = 44100  # sampling rate, Hz, must be integer
volume = 1.0  # range [0.0, 1.0]
duration = 5.0 # in seconds, may be float

# generate samples, note conversion to float32 array
time_dots = np.arange(sr * duration) / sr
samples = (np.sin(2 * np.pi * f * time_dots))
samples += (np.sin(4 * np.pi * f * time_dots)) * 0.2
samples += (np.sin(6 * np.pi * f * time_dots)) * 0.02
samples += (np.sin(8 * np.pi * f * time_dots)) * 0.002
samples += (np.sin(10 * np.pi * f * time_dots)) * 0.0002
samples = samples.astype(np.float32)

sound = np.int32(samples * (2 ** 31 - 1))
write("test.wav", sr, sound)
