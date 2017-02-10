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
  k=1
  b=3 # 1 , 0.1
  return np.array([ x[1] , -b*x[1]-k*x[0] ])


x0=[0,0.5] #x2 [0.5;2.5]

n=1000
t0=0
te=20


t=np.linspace(t0,te,n)

x=odeint(f,x0,t)
plt.plot(t,x)


x,t=euler(f,x0,[t0,te],0.5)
plt.plot(t,x)

x,t=euler(f,x0,[t0,te],0.1)
plt.plot(t,x)


x,t=euler(f,x0,[t0,te],0.01)
plt.plot(t,x)



plt.show()