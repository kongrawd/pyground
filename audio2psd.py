#!/usr/bin/env python
# Plot the Power Spectral Density of an Audio Source
# Started on Thursday of January 31, 2019 by kongrawd.
# Version of February 13, 2019: Support input of higher bitrate mono audio.

import os, sys
from scipy.io import wavfile
import numpy as np
import matplotlib
matplotlib.use('TkAgg')     # rendering backend: macOS
import matplotlib.pyplot as plt

filename = 'speech/TH_th-thaiweather1_cut2.wav'

# obtain path in the same folder of the script
from os import path
audio_file = path.join(os.path.abspath(os.path.dirname(sys.argv[0])), filename)
fs, data = wavfile.read(audio_file)

# subplot grid magic
fig = plt.figure(figsize=(6, 4))
# use matplotlib to estimate and plot the PSD
plt.subplot(2,1,1).psd(data, NFFT=512, Fs=fs, Fc=0)
startPSD, endPSD = plt.subplot(2,1,1).get_xlim()
interval_tick = np.around(fs/20, decimals=-2)
plt.subplot(2,1,1).set_xticks(np.arange(0, endPSD, interval_tick)) 
plt.subplot(2,1,1).set_xlabel('Frequency (Hz)')
plt.subplot(2,1,1).set_ylabel('Relative Power (dB)')
# input signal
plt.subplot(2,2,3).plot(data)
plt.subplot(2,2,3).set_title('Waveform') 
plt.subplot(2,2,3).set_xlabel('Sample')
plt.subplot(2,2,3).set_ylabel('Amplitude')
# spectogram
plt.subplot(2,2,4).specgram(data, NFFT=2048, Fs=fs)  
plt.subplot(2,2,4).set_title('Spectrogram')  
plt.subplot(2,2,4).set_xlabel('Time (s)')  
plt.subplot(2,2,4).set_ylabel('Frequency (Hz)')  

# show plot
plt.tight_layout()
fig.subplots_adjust(top=0.88)
fig.suptitle('PSD of '+filename)
# save plot
plt.savefig(filename+'.png', dpi=300)
plt.show()
