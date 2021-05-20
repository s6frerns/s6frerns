import numpy as np

from matplotlib import pyplot as plt
from scipy import integrate
import csv
import glob, os
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd
import time
start = time.time()
os.chdir('/data/linac2/klystron/th2100d-210038')
list=[]
Flaeche=[]
Flaeche1=[]
Flaeche2=[]
Flaeche3=[]

for file in glob.glob("*.dat"):

    a=len(file)
    if a==14:
        list.append(file)

for i in list:
    data = np.loadtxt(i)

    # plt.plot(data[:,0],data[:,1],'bo')
    x = data[:, 1]
    a = data[:, 2] * 2000
    b = data[:, 3] * 30000
    c = data[:, 4] / 0.05
    d = data[:, 5] / 0.035

    q=integrate.simps(a, x)
    q1 = integrate.simps(b, x)
    q2= integrate.simps(c, x)
    q3 = integrate.simps(d, x)

    Flaeche.append(q)
    Flaeche1.append(q1)
    Flaeche2.append(q2)
    Flaeche3.append(q3)
arr = np.array(Flaeche)
arr1 = np.array(Flaeche1)
arr2 = np.array(Flaeche2)
arr3 = np.array(Flaeche3)

Integral= {'PVN-Spannung': Flaeche,
        'Klystron-Spannung': Flaeche1,
        'Klystron-Strom':Flaeche2,
        'Klystron-Stom(500 Ohm)':Flaeche3
        }
df = pd.DataFrame(Integral, columns= ['PVN-Spannung', 'Klystron-Spannung','Klystron-Strom','Klystron-Stom(500 Ohm)'])
df.to_csv (r'/home/ernst/Dokumente/Plot/Integral.csv', index = False, header=True, sep='\t')
ende = time.time()
print('{:5.3f}s'.format(ende-start))




