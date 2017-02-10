#/usr/bin/python

import numpy as np
import matplotlib
matplotlib.use("Tkagg")
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from RichtungsFeld import RichtungsFeld



def f(x,t):
  k=1
  return [x[1], -k*np.sin(x[0])]

x0=[0,1.5]
n=100
t0=0
te=20

plt.figure()
t=np.linspace(t0,te,n)
x=odeint(f,x0,t)
plt.plot(x[:,0],x[:,1])

plt.figure()
plt.plot(t,x[:,1])
plt.plot(t,x[:,0])

#b

def f2(x,t):
  k=1
  return [x[1], -k*x[0]]

def e(x,t):
  k=1
  x[1]/np.sqrt(k)*np.sin(np.sqrt(k)*t)+x[0]*np.cos(np.sqrt(k)*t)

plt.figure()
t=np.linspace(t0,te,n)
x=odeint(f2,x0,t)
plt.plot(x[:,0],x[:,1])

plt.figure()
t=np.linspace(t0,te,n)
x=odeint(e,x0,t)
plt.plot(x[:,0],x[:,1])

plt.show()