# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 19:45:34 2018

@author: Amministratore
"""


def orizzontali(ftesto):
    s = ''
    parole = []
    for lettera in matrice(ftesto):
        s += lettera
        if lettera in elencoParole(ftesto)[0]:
                parole.append(s)
                s += lettera
                if s in elencoParole(ftesto):
                    return parole
                else:
                    s -= lettera
                    if s in elencoParole(ftesto):
                        return parole
    elencoParole(ftesto).remove(parole)
    return parole