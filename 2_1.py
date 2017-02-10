#/usr/bin/python

import numpy as np
import matplotlib
matplotlib.use("Tkagg")
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from RichtungsFeld import RichtungsFeld
from mpl_toolkits.mplot3d import Axes3D


def f(x,t):
  return [x[1], -2*np.cos(x[2])/np.sin(x[2])*x[1]*x[3], x[3], np.sin(x[2])*np.cos(x[2])*x[1]*x[1]-np.sin(x[2])]

def corTrans(phi,psy):
  return [np.cos(phi)*np.sin(psy), np.sin(phi)*np.sin(psy)]

x0=[0,0.1,1,0]

n=1000
t0=0
te=100




t=np.linspace(t0,te,n)
xl=odeint(f,x0,t)

x=corTrans(xl[:,0],xl[:,2])

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

plt.plot(x[0],x[1])
plt.show()