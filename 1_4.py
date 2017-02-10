#/usr/bin/python

import numpy as np
import matplotlib
matplotlib.use("Tkagg")
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from RichtungsFeld import RichtungsFeld


global a, g

a=0.7
g=1.5



def f(x,t):    
    ret=a*x*(g-x)
    return ret

RichtungsFeld(f,[0,10],[0,10])

t = np.linspace(0,10,100)
sol = odeint(f,[1.0,10.0],t)

plt.plot(t,sol[:,0])
plt.show()