import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate
import csv
import glob, os
from matplotlib.backends.backend_pdf import PdfPages
with open('innovators.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Name", "Contribution"])
x=np.arange(100)
y=x*x
a=integrate.simps(y,x)
print(a)