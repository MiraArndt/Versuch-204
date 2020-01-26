
import matplotlib.pyplot as plt
import numpy as np
import csv


#Anzahn,E1,E2,E3,E4,E5,E6,E7,E8,t = np.genfromtxt('content/versuch.txt', unpack=True)
M1 = np.genfromtxt("content/Data/1.csv",unpack=True,usecols=1)
M2 = np.genfromtxt("content/Data/1.csv",unpack=True,usecols=2)
t  = np.genfromtxt("content/Data/1.csv",unpack=True,usecols=9)

plt.plot(t, M2-M1, label='T2-T1')

plt.xlabel(r'$t\:/\: \si{\second}$')
plt.ylabel(r'$T \:/\: \si{\celsius}$')
plt.legend(loc='best')


plt.savefig('build/diff1.pdf')
