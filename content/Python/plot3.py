import matplotlib.pyplot as plt
import numpy as np
import csv
from uncertainties import ufloat
import uncertainties.unumpy as unp

#Anzahn,E1,E2,E3,E4,E5,E6,E7,E8,t = np.genfromtxt('content/versuch.txt', unpack=True)
M1 = np.genfromtxt("content/Data/2.csv",unpack=True,usecols=1)
M2 = np.genfromtxt("content/Data/2.csv",unpack=True,usecols=2)
t  = np.genfromtxt("content/Data/2.csv",unpack=True,usecols=9)

Af=ufloat(1.13,0.07)
An=ufloat(3.49,0.07)
t1=ufloat(16.1,1.3)

print(377*8400*(0.03)**2/(2*t1*unp.log(An/Af)))

plt.plot(t, M1, label='T1')
plt.plot(t, M2, label='T2')
plt.xlabel(r'$t\:/\: \si{\second}$')
plt.ylabel(r'$T \:/\: \si{\celsius}$')
plt.legend(loc='best')


plt.savefig('build/plot3.pdf')
