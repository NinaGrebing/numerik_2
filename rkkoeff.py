# -*- coding: utf-8 -*-
"""
NDGL1

Butcher-Schemata

Aufruf:  rkkoeff("euler")

Implementiert sind:
    euler, collatz, rk4, k38, rk43, dp54, rkf23

"""

from scipy import array

def rkkoeff(name):
    def euler():
        return array([[0,0], \
                      [0,1] ], dtype=float)
                
    def collatz():
        return array([[  0 , 0 ,0], \
                      [ 1./2,1./2,0], \
                      [  0 , 0 ,1] ], dtype=float) 
    
        
    def rk4():
        return array([[  0 ,  0 ,  0 ,  0 ,  0], \
                      [ 1./2, 1./2,  0 ,  0 ,  0], \
                      [ 1./2,  0 , 1./2,  0 ,  0], \
                      [  1 ,  0 ,  0 ,  1 ,  0], \
                      [  0 , 1./6, 1./3, 1./3, 1./6]], dtype=float)
    
      
    def k38():
        return array([[  0 ,   0 ,  0 ,  0 ,  0],\
                      [ 1./3,  1./3,  0 ,  0 ,  0],\
                      [ 2./3, -1./3,  1 ,  0 ,  0],\
                      [  1 ,   1 , -1 ,  1 ,  0],\
                      [  0 ,  1./8, 3./8, 3./8, 1./8]], dtype=float)
    
        
        
    def rk43():
        # abbc = rk43()
        #  Koeffizienten RKF 4(3)
        #  klassischer RK4 auf 5 Stufen aufgebohrt und 3.Ordnung eingebettet
        #  Deuflhard./Bornemann S.208
        #  letzte beiden Koeffizienten in der ersten Spalte sind Konsistenzordnungen
        
        return array([\
             [ 0 ,     0 ,     0 ,     0 ,     0,    0],\
             [1./2,    1./2,     0 ,     0 ,     0,    0],\
             [1./2,     0 ,    1./2,     0 ,     0,    0],\
             [ 1 ,     0 ,     0 ,     1 ,     0,    0],\
             [ 1 ,    1./6,    1./3,    1./3,    1./6,   0],\
             [ 4 ,    1./6,    1./3,    1./3,    1./6,   0],\
             [ 3 ,    1./6,    1./3,    1./3,     0 ,  1./6]], dtype=float)


    def dp54():
        # abbc = dp54()
        #  Koeffizienten Dormand-Prince 5(4)
        #  Hairer./Wanner, Band 1, S. 171 (bzw. Deuflhard./Bornemann S.209)
        #  letzte beiden Koeffizienten in der ersten Spalte sind Konsistenzordnungen
        
        return array([\
             [ 0   ,        0   ,        0   ,        0   ,        0   ,        0   ,        0   ,        0  ],\
             [1./5   ,      1./5   ,       0   ,        0   ,        0   ,        0   ,        0   ,        0  ],\
             [3./10   ,     3./40   ,     9./40   ,      0   ,        0   ,        0   ,        0   ,        0  ],\
             [4./5   ,     44./45   ,   -56./15   ,    32./9   ,       0   ,        0   ,        0   ,        0  ],\
             [8./9  ,   19372./6561 ,-25360./2187 , 64448./6561 ,  -212./729   ,     0   ,        0   ,        0  ],\
             [ 1   ,    9017./3168 ,  -355./33   , 46732./5247 ,    49./176  , -5103./18656   ,   0   ,        0  ],\
             [ 1   ,      35./384   ,     0   ,     500./1113 ,   125./192  , -2187./6784   ,  11./84   ,      0  ],\
             [ 5   ,      35./384   ,     0   ,     500./1113 ,   125./192  , -2187./6784   ,  11./84   ,      0  ],\
             [ 4   ,    5179./57600   ,   0   ,    7571./16695,   393./640  ,-92097./339200 , 187./2100   ,   1./40]], dtype=float)



    def rkf23():
        # abbc = rkf23()
        #  Koeffizienten RKF2(3)
        #  letzte beiden Koeffizienten in der ersten Spalte sind Konsistenzordnungen
        
        return array([\
             [ 0    ,       0    ,       0    ,       0 ],\
             [ 1    ,       1    ,       0    ,       0 ],\
             [1./2    ,     1./4    ,     1./4    ,      0 ],\
             [ 2    ,      1./2    ,     1./2    ,      0 ],\
             [ 3    ,      1./6    ,     1./6    ,     2./3]], dtype=float)

    return eval(name+'()')
#    return eval(name)