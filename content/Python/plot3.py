import matplotlib.pyplot as plt
import numpy as np
import csv


#Anzahn,E1,E2,E3,E4,E5,E6,E7,E8,t = np.genfromtxt('content/versuch.txt', unpack=True)
M1 = np.genfromtxt("content/Data/2.csv",unpack=True,usecols=1)
M2 = np.genfromtxt("content/Data/2.csv",unpack=True,usecols=2)
t  = np.genfromtxt("content/Data/2.csv",unpack=True,usecols=9)

plt.plot(t, M1, label='T1')
plt.plot(t, M2, label='T2')
plt.xlabel(r'$t\:/\: \si{\second}$')
plt.ylabel(r'$T \:/\: \si{\celsius}$')
plt.legend(loc='best')


plt.savefig('build/plot3.pdf')
