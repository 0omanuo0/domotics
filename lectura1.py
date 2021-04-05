#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""programa de control de riego, con todos los modos"""
__author__  = "Manuel Serrano"
__version__ = "1.1"
import pickle
def leer():
    try:
        fichero = open("archivo_epiko", "rb")
        e = pickle.load(fichero)
        del(fichero)
    except:
        e = [False,False,False,False,False]
    return e
def escribir(tipo, dato):
    a = leer()
    print(a)
    if(tipo == "riego"):
        a[0] = dato
    elif(tipo == "manual"):
        a[1] = dato
    elif(tipo == "off"):
        a[2] = dato
    elif(tipo == "zonaAct"):
        a[3] = dato
    fichero = open("archivo_epiko", "wb")
    pickle.dump(a, fichero)
    del(fichero)
#escribir("riego", True)
'''fichero = open("archivo_epiko", "wb")
pickle.dump([False,False,False,False,False], fichero)
del(fichero)'''
print(leer())