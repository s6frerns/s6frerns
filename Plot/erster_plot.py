import numpy as np
from matplotlib import pyplot as plt

data = np.loadtxt('1597313484.dat')

x=data[:,1]
a=data[:,2]*2000
b=data[:,3]*30000
c=data[:,4]*0.05
d=data[:,5]*0.035

fig, axs = plt.subplots(2, 2)

axs[0, 1].plot(x,a ,':ro')
plt.setp(axs[0, 1], xlabel='t in s')
plt.setp(axs[0, 1], ylabel='U in V')
axs[0,1].set_title('PVN-Spannung')
#########################################################################
axs[0, 0].plot(x,b,':y')
plt.setp(axs[0, 0], xlabel='t in s')
plt.setp(axs[0, 0], ylabel='U in V')
axs[0,0].set_title('Klystron-Spannung')
################################################################
axs[1, 0].plot(x,c,':b')
plt.setp(axs[1, 0], xlabel='t in s')
plt.setp(axs[1, 0], ylabel='I in A')
axs[1,0].set_title('Klystron-Strom')
##############################################################
axs[1, 1].plot(x,d,':b')
plt.setp(axs[1, 1], xlabel='t in s')
plt.setp(axs[1, 1], ylabel='I in A')
axs[1,1].set_title('Klystron-Stom(500 Ohm)')
##############################################################
fig.tight_layout()

plt.legend()
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
plt.show()