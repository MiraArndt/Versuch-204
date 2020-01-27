import matplotlib.pyplot as plt
import numpy as np
import csv
from uncertainties import ufloat
import uncertainties.unumpy as unp

#Anzahn,E1,E2,E3,E4,E5,E6,E7,E8,t = np.genfromtxt('content/versuch.txt', unpack=True)
E1 = np.genfromtxt("content/Data/3.csv",unpack=True,usecols=7)
E2 = np.genfromtxt("content/Data/3.csv",unpack=True,usecols=8)
t  = np.genfromtxt("content/Data/3.csv",unpack=True,usecols=9)

Af=ufloat(1.01,0.08)
An=ufloat(6.02,0.09)
t1=ufloat(75,5)


print(470*7900*(0.03)**2/(2*t1*unp.log(An/Af)))

plt.plot(t, E1, label='T7')
plt.plot(t, E2, label='T8')
plt.xlabel(r'$t\:/\: \si{\second}$')
plt.ylabel(r'$T \:/\: \si{\celsius}$')
plt.legend(loc='best')


plt.savefig('build/plot5.pdf')
