import matplotlib.pyplot as plt
import numpy as np
import csv
from uncertainties import ufloat
import uncertainties.unumpy as unp

#Anzahn,E1,E2,E3,E4,E5,E6,E7,E8,t = np.genfromtxt('content/versuch.txt', unpack=True)
A5 = np.genfromtxt("content/Data/2.csv",unpack=True,usecols=5)
A6 = np.genfromtxt("content/Data/2.csv",unpack=True,usecols=6)
t  = np.genfromtxt("content/Data/2.csv",unpack=True,usecols=9)

Af=ufloat(2.04,0.09)
An=ufloat(3.62,0.05)
t1=ufloat(9.1,0.9)

print(900*2700*(0.03)**2/(2*t1*unp.log(An/Af)))

plt.plot(t, A5, label='T5')
plt.plot(t, A6, label='T6')
plt.xlabel(r'$t\:/\: \si{\second}$')
plt.ylabel(r'$T \:/\: \si{\celsius}$')
plt.legend(loc='best')


plt.savefig('build/plot4.pdf')
