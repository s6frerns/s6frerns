import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import csv
from scipy import integrate
pp = PdfPages('multipage.pdf')
import glob, os

os.chdir('/data/linac2/klystron/th2100d-210038')
list=[]


for file in glob.glob("*.dat"):

    a=len(file)
    if a==14:
        list.append(file)

print(list)
for i in list:
    data = np.loadtxt(i)

    # plt.plot(data[:,0],data[:,1],'bo')
    x = data[:, 1]
    a = data[:, 2] * 2000
    b = data[:, 3] * 30000
    c = data[:, 4] / 0.05
    d = data[:, 5] / 0.035

    fig, axs = plt.subplots(2, 2)
    fig.suptitle(i, fontsize=16)
    axs[0, 1].plot(x, a, ':ro')
    plt.setp(axs[0, 1], xlabel='t in s')
    plt.setp(axs[0, 1], ylabel='U in V')
    axs[0, 1].set_title('PVN-Spannung')
    #print(integrate.simps(x, a))

    #########################################################################
    axs[0, 0].plot(x, b, ':y')
    plt.setp(axs[0, 0], xlabel='t in s')
    plt.setp(axs[0, 0], ylabel='U in V')
    axs[0, 0].set_title('Klystron-Spannung')
    ################################################################
    axs[1, 0].plot(x, c, ':b')
    plt.setp(axs[1, 0], xlabel='t in s')
    plt.setp(axs[1, 0], ylabel='I in A')
    axs[1, 0].set_title('Klystron-Strom')
    ##############################################################
    axs[1, 1].plot(x, d, ':b')
    plt.setp(axs[1, 1], xlabel='t in s')
    plt.setp(axs[1, 1], ylabel='I in A')
    axs[1, 1].set_title('Klystron-Stom(500 Ohm)')
    ##############################################################



    ###############################################################
    fig.tight_layout()


    plt.savefig(pp, format='pdf')

    plt.show()

pp.close()