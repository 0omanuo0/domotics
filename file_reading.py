#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""programa de control de riego, con todos los modos"""
__author__  = "Manuel Serrano"
__version__ = "1.1"

import pickle

def read():#read all
    try:
        file = open("archivo_epiko", "rb")
        e = pickle.load(file)
        del(file)
    except:
        e = "E4"
    return e
    
def readArea(area):#read specific area
    All = read()
    return All[area]





'''    
escribirParam("riego", True)
print(leer())
''''''
nombreSub1 = ["cesped1", "cesped2", "casped3"]
pinSub1 = [1,2,3]
tSub1 = [10, 13, 12]
week1 = {0:True, 1:True, 2:False, 3:True, 4:True, 5:False, 6:True}
Sub1 = [nombreSub1, pinSub1, tSub1, week1]

nombreSub2 = ["frontal", "todo lo demas", "olivos"]
pinSub2 = [4,6,5]
tSub2 = [11, 20, 50]
week2 = {0:True, 1:True, 2:True, 3:True, 4:True, 5:True, 6:True}
Sub2 = [nombreSub2, pinSub2, tSub2, week2]



tot = {"Cesped":Sub1, "General":Sub2, "prueba":[]}

ficher = open("archivo_epiko", "wb")
pickle.dump(tot, ficher)
del(ficher)
print("a")
'''