import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from scipy.signal import find_peaks

import csv
from scipy.signal import find_peaks
from scipy import integrate
#pp = PdfPages('fouier.pdf')
import glob, os
from datetime import datetime
from scipy.fft import fft, fftfreq, fftshift
from numpy import diff

x=[]
for i in range(0,800,1):
   x.append(i)
x=np.array(x)
y=np.sin(x)


Fs=len(y) #sample
t=x[1]-x[0]#sampling distance





yf=np.fft.fft(y)
xf1 = np.fft.fftfreq(Fs, t)

peaks = find_peaks(yf, height=1, threshold=1, distance=1)
height = peaks[1]['peak_heights']  # list of the heights of the peaks
peak_pos = xf1[peaks[0]]  # list of the peaks positions

#print(peak_pos)



fig, (ax1, ax2) = plt.subplots(2)
ax2.plot(xf1, abs(yf)**2)
ax2.scatter(peak_pos, height, color='r', s=15, marker='D', label='Maxima')
print(peak_pos)
ax1.plot(x, y)



plt.yscale("log")
plt.legend()
plt.grid()
plt.show()

