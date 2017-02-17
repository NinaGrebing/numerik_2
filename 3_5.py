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
import rkkoeff as rk

  
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
    
    # Collatz-Schritt    
        un = u+h*f(u+h/2*f(u,t),t+h/2)#u + h * f(u,t)
      
        t  = tn
        u  = un
        
        tv = append(tv, t)
        uv = vstack((uv,  u))
    return (uv, tv)
  
  
  
  
  
def rkskalar(f, u0, T, abc, h):
  t0 = T[0]
  te = T[1]
  
  u0 = array(u0).flatten()
  
  tv = t0
  uv = u0.T
  
  t = t0
  u = u0[0]
  
  d=abc.shape
  
  s=d[0]-1
  #A=abc[0:s-1,1:s]
  #b=abc[0:s-1,0]
  #c=abc[s-1,1:s]
  
  A=abc[0:s,1:s+1]
  c=abc[0:s,0]
  b=abc[s,1:s+1]
  
  k=np.zeros(s)
  un=0

  ttol = 1e-8 * h 
  while t<te:
    tn = t + h
    if tn > te-ttol:
      tn = te
      h  = tn - t

    for i in range(0,s):
      z=0
      for j in range(0,i):
	z+=A[i][j]*k[j]
      k[i]=f(t+c[i]*h,
	     [u0[0]+h*z,u0[1]+z*h])
      
    #phi(t+h,t,y)=y+h* z[i=1][s](b_i*k_i)
  
    z2=0
    for l in range(0,s):
      z2+=b[l]*k[l]

    un+=h*z2  
  
    t  = tn
    u  = un
        
    tv = append(tv, t)
    uv = vstack((uv,  u))
  
  return (uv, tv)

def f(x,t):
  k=1
  b=0.1
  return np.array([ x[1] , -b*x[1]-k*x[0] ])
  
  
x0=[0,0]

t0=0
te=100
n=1000

t=np.linspace(t0,te,n)

h=0.25#0.25,0.1,0.05


abc=rk.rkkoeff("k38")

#x=odeint(f,x0,[t0,te])
#plt.plot(t,x[:,0],label="Odeint")


x,t=rkskalar(f,x0,[t0,te],abc,h)
plt.plot(t,x[:,0],label="Runge-Kutta")


plt.legend()
plt.show()












