import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import csv
from scipy import integrate
from scipy.signal import find_peaks
pp = PdfPages('fouier_ruck.pdf') # name for the pdf wich contains all the analysis
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

    #reading data from file
    data = np.loadtxt(i)

    x = data[:, 1]
    a = data[:, 2] * 2000
    b = data[:, 3] * 30000
    c = data[:, 4] / 0.05
    d = data[:, 5] / 0.035

##Here starts the fouier trafo
###############################################################
    Fs=len(a) #sample
    t = (x[0] - x[-1]) / Fs#sampling distance
#################################################################
    yf = np.fft.fft(a)
    xf1 = np.fft.fftfreq(Fs, t)
    #print(yf)


    ruckx=[]
    rucky=[]
    for p in range(len(xf1)):
        if np.any(xf1>0) and np.any(xf1<1e7):
            ruckx.append(xf1)
            rucky.append(yf)

    print(rucky)



#####################################################################
##in this section is the back trafo defined

    #yb=np.fft.ifft(yf)
    #xb=np.fft.ifft(xf1)






##########################################################################
    #plot section
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