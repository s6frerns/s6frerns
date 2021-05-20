import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
a=np.array([0,1,2,3,4,5])
print(len(a))
# sampling information
Fs = 500 # sample rate  länge des arrays

T = 1/Fs # sampling period
t = 0.1 # seconds of sampling abstand zwischen  punkten
N = Fs*t # total points in signal
print(N)
# signal information
freq = 100 # in hertz, the desired natural frequency
omega = 2*np.pi*freq # angular frequency for sine waves

t_vec = np.arange(N)*T # time vector for plotting x werte
y = np.sin(omega*t_vec) # y werte

plt.plot(t_vec,y)
plt.show()