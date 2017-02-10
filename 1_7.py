#/usr/bin/python

import numpy as np
import matplotlib
matplotlib.use("Tkagg")
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from RichtungsFeld import RichtungsFeld



def f(x,t):
  k=1
  b=0.1
  return [x[1], -b*x[1]-k*np.sin(x[0])]

x0=[0,1.5]
n=1000
t0=0
te=100

plt.figure()
t=np.linspace(t0,te,n)
x=odeint(f,x0,t)
plt.plot(x[:,0],x[:,1])

plt.figure()
plt.plot(t,x[:,1])
plt.plot(t,x[:,0])

plt.show()