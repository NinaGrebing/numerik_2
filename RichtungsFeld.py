# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 17:27:55 2017

@author: Grajewski
"""

from pylab import *
import matplotlib.pyplot as plt
import numpy as np

def RichtungsFeld(f, T, X):
    # Eingaben
    #f: rechte Seite der Differentialgleichung
    # T = [t0, te] : Zeitintervall
    # X = [x0, x1] : Wertebereich
    
    m = 20
    n = 20
    
    t0 = T[0]
    te = T[1]
    
    x0 = X[0]
    x1 = X[1]
    
    tvec = np.linspace(t0, te, m)
    xvec = np.linspace(x0, x1, n)
    
    tt, xx = np.meshgrid(tvec, xvec)

    T_component = np.ones([m,n])

    vecf = np.vectorize(f)

    X_component  = vecf(xx, tt)
    
    plt.figure()
    plt.quiver(tt, xx, T_component, X_component, color='0.5', angles='xy')
