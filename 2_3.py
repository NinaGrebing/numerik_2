#/usr/bin/python

import numpy as np
import matplotlib
matplotlib.use("Tkagg")
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from RichtungsFeld import RichtungsFeld
from mpl_toolkits.mplot3d import Axes3D
from euler import euler


def f(x,t):
  a=0.001
  g=100
  return a*x*(g-x)


x0=10
x1=200

n=1000
t0=0
te=100


t=np.linspace(t0,te,n)

x=odeint(f,x0,t)
plt.plot(t,x)


x,t=euler(f,x0,[t0,te],10)
plt.plot(t,x)


x,t=euler(f,x0,[t0,te],2)
plt.plot(t,x)

x,t=euler(f,x0,[t0,te],1)
plt.plot(t,x)

x,t=euler(f,x0,[t0,te],0.5)
plt.plot(t,x)

plt.show()