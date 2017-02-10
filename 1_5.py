#/usr/bin/python

import numpy as np
import matplotlib
matplotlib.use("Tkagg")
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from RichtungsFeld import RichtungsFeld



x_0=[1,1]
x_1=[2,1]
x_2=[5,1]

x0=x_0

def f(x,t):
  alpha= lambda b: 2-b
  gamma= lambda r: 1.1
  beta=1
  delta=1
  return [alpha(x[0])*x[0]-beta*x[0]*x[1], -gamma(x[1])*x[1]+delta*x[0]*x[1]]

def f1(x,t):
  alpha= lambda b: 2
  gamma= lambda r: 1
  beta=1
  delta=0.2
  return [alpha(x[0])*x[0]-beta*x[0]*x[1], -gamma(x[1])*x[1]+delta*x[0]*x[1]]

def f2(x,t):
  alpha= lambda b: (2-b)*(1.5*x[0]*(x[0]-1)+1)
  gamma= lambda r: 1.1
  beta=1
  delta=1
  return [alpha(x[0])*x[0]-beta*x[0]*x[1], -gamma(x[1])*x[1]+delta*x[0]*x[1]]

n=100
t0=0
te=10

plt.figure()
t=np.linspace(t0,te,n)
x=odeint(f,x0,t)
plt.plot(x[:,0],x[:,1])

plt.figure()
t=np.linspace(t0,te,n)
x=odeint(f1,x0,t)
plt.plot(x[:,0],x[:,1])

plt.figure()
t=np.linspace(t0,te,n)
x=odeint(f2,x0,t)
plt.plot(x[:,0],x[:,1])

#############################################
x0=x_1

plt.figure()
t=np.linspace(t0,te,n)
x=odeint(f,x0,t)
plt.plot(x[:,0],x[:,1])

plt.figure()
t=np.linspace(t0,te,n)
x=odeint(f1,x0,t)
plt.plot(x[:,0],x[:,1])

plt.figure()
t=np.linspace(t0,te,n)
x=odeint(f2,x0,t)
plt.plot(x[:,0],x[:,1])

#############################################
x0=x_2

plt.figure()
t=np.linspace(t0,te,n)
x=odeint(f,x0,t)
plt.plot(x[:,0],x[:,1])

plt.figure()
t=np.linspace(t0,te,n)
x=odeint(f1,x0,t)
plt.plot(x[:,0],x[:,1])

plt.figure()
t=np.linspace(t0,te,n)
x=odeint(f2,x0,t)
plt.plot(x[:,0],x[:,1])

plt.show()