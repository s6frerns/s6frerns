import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import csv
from scipy import integrate
from scipy.signal import find_peaks
pp = PdfPages('fouier.pdf')
import glob, os
from scipy.optimize import curve_fit
#from scipy import asarray as ar,exp
from datetime import datetime
from scipy.fft import fft, fftfreq, fftshift
from numpy import diff

os.chdir('/data/linac2/klystron/th2100d-210038')
list=[]


for file in glob.glob("*.dat"):
    a=len(file)
    if a==14:
        list.append(file)

for i in list:
    data = np.loadtxt(i)

    x = data[:, 1]
    a = data[:, 2] * 2000
    b = data[:, 3] * 30000
    c = data[:, 4] / 0.05
    d = data[:, 5] / 0.035

###############################################################
    Fs=len(a) #sample
    t=(x[0]-x[-1])/Fs #sampling distance
#################################################################


    yf = np.fft.fft(a)
    xf1 = np.fft.fftfreq(Fs, t)

   # peaks = find_peaks(yf, height=1, threshold=1, distance=1)
   # height = peaks[1]['peak_heights']  # list of the heights of the peaks
   # peak_pos = xf1[peaks[0]]  # list of the peaks positions

#################################################################
   # yg = np.fft.fft(b)
    #xf2 = np.fft.fftfreq(Fs, t)


    #peaks1 = find_peaks(yg, height=1, threshold=1, distance=1)
   # height1 = peaks1[1]['peak_heights']  # list of the heights of the peaks
   # peak_pos1 = xf2[peaks1[0]]  # list of the peaks positions
##################################################################
    #yh = np.fft.fft(c)
    #xf3 = np.fft.fftfreq(Fs, t)

    #peaks2 = find_peaks(yh, height=1, threshold=1, distance=1)
    #height2 = peaks2[1]['peak_heights']  # list of the heights of the peaks
    #peak_pos2 = xf3[peaks2[0]]  # list of the peaks positions
#################################################################
    #yj = np.fft.fft(d)
    #xf4 = np.fft.fftfreq(Fs, t)

    #peaks3 = find_peaks(yj, height=1, threshold=1, distance=1)
    #height3 = peaks3[1]['peak_heights']  # list of the heights of the peaks
    #peak_pos3 = xf4[peaks2[0]]  # list of the peaks positions


#####################################################################

    fig, (ax1, ax2) = plt.subplots(2)

    ax1.plot(x, a)
    ax2.plot(abs(xf1), abs(yf)**2)

    fig.suptitle(i, fontsize=16)
    ax1.set_xlabel('t in s')
    ax1.set_ylabel('U in V')
    ax1.set_title('PVN-Spannung')
    ax2.set_xlabel('f in Hz')
    fig.tight_layout()

    plt.yscale("log")
    plt.xlim(0, 1e7)
    plt.grid()
    plt.savefig(pp, format='pdf')
    plt.show()


pp.close()