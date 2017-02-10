# -*- coding: utf-8 -*-
"""
Numerik 2, explizites Euler-Verfahren 


"""

from scipy import array, append, vstack

def euler(f, u0, T, h):
    """ 
    uv, tv = euler(f, u0, T, h)
    
    Euler-Verfahren mit fester Schrittweite
       
    IN:
        f(u,t) : muss array auf array abbilden
        
        T      : [t0,te]
        
        u0     : Startwert (array)
        
        h      : Zeitschrittweite
        
    OUT:
        uv     : Lösungskomponenten (Spalten) des arrays

        tv     : array
        
    t0 und te sind sicher im Output
    """
    
    # Start- und Endzeit ermitteln
    t0 = T[0]
    te = T[1]
    
    # Anfangswert ggf. auf Zeilenvektor transformieren
    u0 = array(u0).flatten()
    
    # Anfangszeit und -wert in Lösungsvektor eintragen
    tv = t0
    uv = u0.T
    
    
    # eigentliches Verfahren
    t = t0
    u = u0
    
    ttol = 1e-8 * h # Toleranz für Schlussschritt 
    
    while t<te:
    # Letzten Schritt evtl. verkürzen, damit man genau auf te landet
        tn = t + h
        if tn > te-ttol:
            tn = te
            h  = tn - t
    
    # Euler-Schritt    
        un = u + h * f(u,t)
    
    # neuer Zeitpunkt und neue Näherung übernehmen    
        t  = tn
        u  = un
        
    # aktuelles Ergebnis an den Ergbnisvektor anhängen
        tv = append(tv, t)
        uv = vstack((uv,  u))
    
    return (uv, tv)