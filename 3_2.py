#/usr/bin/python

import numpy as np
import matplotlib
matplotlib.use("Tkagg")
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from RichtungsFeld import RichtungsFeld
from mpl_toolkits.mplot3d import Axes3D
from euler import euler
from scipy import array, append, vstack

  
def collatz(f, u0, T, h):
    t0 = T[0]
    te = T[1]
    
    # Anfangswert ggf. auf Zeilenvektor transformieren
    u0 = array(u0).flatten()
    
    tv = t0
    uv = u0.T
    
    
    # eigentliches Verfahren
    t = t0
    u = u0
    
    ttol = 1e-8 * h 
    
    while t<te:
        tn = t + h
        if tn > te-ttol:
            tn = te
            h  = tn - t
    
    # Euler-Schritt    
        un = u+h*f(u+h/2*f(u,t),t+h/2)#u + h * f(u,t)
      
        t  = tn
        u  = un
        
        tv = append(tv, t)
        uv = vstack((uv,  u))
    return (uv, tv)
  
def heun(f, u0, T, h):
    
    t0 = T[0]
    te = T[1]
    
    # Anfangswert ggf. auf Zeilenvektor transformieren
    u0 = array(u0).flatten()
    
    tv = t0
    uv = u0.T
    
    
    # eigentliches Verfahren
    t = t0
    u = u0
    
    ttol = 1e-8 * h
    
    while t<te:
        tn = t + h
        if tn > te-ttol:
            tn = te
            h  = tn - t
    
    # Euler-Schritt    
        un = u+h/2*(f(u,t)+f(u+h*f(u,t),tn))
       
        t  = tn
        u  = un
        
        tv = append(tv, t)
        uv = vstack((uv,  u))
    return (uv, tv)
  
  
def f(x,t):
  k=1
  b=1#0.1,3
  return np.array([ x[1] , -b*x[1]-k*x[0] ])

u=1.5
v=0

x0=[u,v]
  
t0=0
te=20
n=1000

t=np.linspace(t0,te,n)

h=0.5#0.1,0.01

x,t=euler(f,x0,[t0,te],h)
plt.plot(t,x)

x,t=collatz(f,x0,[t0,te],h)
plt.plot(t,x)

x,t=heun(f,x0,[t0,te],h)
plt.plot(t,x)

plt.show()












