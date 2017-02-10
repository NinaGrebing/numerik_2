#/usr/bin/python

import numpy as np
import matplotlib
matplotlib.use("Tkagg")
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from RichtungsFeld import RichtungsFeld
from mpl_toolkits.mplot3d import Axes3D


def f(x,t):
  s=10
  b=8./3.
  r=28
  return [ -s*x[0]+s*x[1] , -x[0]*x[2]+r*x[0]-x[1] , x[0]*x[1]-b*x[2] ]


x0=[-8,8,27]

n=10000
t0=0
te=100


t=np.linspace(t0,te,n)

x=odeint(f,x0,t)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plt.plot(x[:,0],x[:,1],x[:,2])
plt.show()