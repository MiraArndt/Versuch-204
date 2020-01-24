
import matplotlib.pyplot as plt
import numpy as np
import csv


#Anzahn,E1,E2,E3,E4,E5,E6,E7,E8,t = np.genfromtxt('content/versuch.txt', unpack=True)
M1 = np.genfromtxt("content/Data/1.csv",unpack=True,usecols=1)
M4 = np.genfromtxt("content/Data/1.csv",unpack=True,usecols=4)
t  = np.genfromtxt("content/Data/1.csv",unpack=True,usecols=9)

plt.plot(t, M1, label='T1')
plt.plot(t, M4, label='T4')
plt.xlabel(r'$t\:/\: \si{\second}$')
plt.ylabel(r'$T \:/\: \si{\celsius}$')
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot1.pdf')
