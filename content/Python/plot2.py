import matplotlib.pyplot as plt
import numpy as np
import csv


#Anzahn,E1,E2,E3,E4,E5,E6,E7,E8,t = np.genfromtxt('content/versuch.txt', unpack=True)
A5 = np.genfromtxt("content/Data/1.csv",unpack=True,usecols=5)
E8 = np.genfromtxt("content/Data/1.csv",unpack=True,usecols=8)
t  = np.genfromtxt("content/Data/1.csv",unpack=True,usecols=9)

plt.plot(t, A5, label='T5')
plt.plot(t, E8, label='T8')
plt.xlabel(r'$t\:/\: \si{\second}$')
plt.ylabel(r'$T \:/\: \si{\celsius}$')
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot2.pdf')
