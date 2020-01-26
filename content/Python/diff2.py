
import matplotlib.pyplot as plt
import numpy as np
import csv


#Anzahn,E1,E2,E3,E4,E5,E6,E7,E8,t = np.genfromtxt('content/versuch.txt', unpack=True)
E7 = np.genfromtxt("content/Data/1.csv",unpack=True,usecols=7)
E8 = np.genfromtxt("content/Data/1.csv",unpack=True,usecols=8)
t  = np.genfromtxt("content/Data/1.csv",unpack=True,usecols=9)

plt.plot(t, E7-E8, label='T7-T8')

plt.xlabel(r'$t\:/\: \si{\second}$')
plt.ylabel(r'$T \:/\: \si{\celsius}$')
plt.legend(loc='best')


plt.savefig('build/diff2.pdf')
