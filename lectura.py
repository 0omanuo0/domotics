#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""programa de control de riego, con todos los modos"""
__author__  = "Manuel Serrano"
__version__ = "1.1"

import pickle

def leer():#leer completo
    try:
        fichero = open("archivo_epiko", "rb")
        e = pickle.load(fichero)
        del(fichero)
    except:
        e = [[False,False,False,False,False],"error lectura"]
    return e

def leerZonas():#leer la matriz zonas completa
    a = leer()
    return a[1]
def cambiarTiempo(z, t):#cambiar los timpos de una zona concreta
    a = leer()
    d = a[1]
    c = d[z]
    b = c[3]
    if(len(t) != len(b)):
        print("error matriz tiempo zona")
        return 1
    else:
        fichero = open("archivo_epiko", "wb")
        c[3] = t
        d[z] = c
        a[1] = d
        pickle.dump(a, fichero)
        del(fichero)
    return 0
def leerTiempo(z):#leer matriz de una zona concreta
    a = leerZona(z)
    a = a[3]
    return a
    
def leerZona(z):#leer la matriz de una zona completa: nombre de la zona, nombres subzonas, pin subzonas, tiempo subzonas
    a = leer()
    a = a[1]
    return a[z]

def escribirParam(tipo, dato):
    a1 = leer()
    a = a1[0]
    if(tipo == "riego"):
        a[0] = dato
    elif(tipo == "manual"):
        a[1] = dato
    elif(tipo == "off"):
        a[2] = dato
    elif(tipo == "zonaAct"):
        a[3] = dato
    elif(tipo == "next"):
        a[4] = dato
    elif(tipo == "parar"):
        a[5] = dato
    fichero = open("archivo_epiko", "wb")
    a1[0]=a
    pickle.dump(a1, fichero)
    del(fichero)
def leerParam():
    return leer()[0]

'''    
escribirParam("riego", True)
print(leer())

nombreSub1 = ["cesped1", "cesped2", "casped3"]
pinSub1 = [1,2,3]
tSub1 = [10, 13, 12]
Sub1 = ["Cesped", nombreSub1, pinSub1, tSub1]#

nombreSub2 = ["frontal", "todo lo demas", "olivos"]
pinSub2 = [4,6,5]
tSub2 = [11, 20, 50]
Sub2 = ["General",nombreSub2, pinSub2, tSub2]

Sub3 = ["prueba"]

ficher = open("archivo_epiko", "wb")
pickle.dump([[False,False,True,False,False, False],[Sub1,Sub2,Sub3]], ficher)
del(ficher)
'''
