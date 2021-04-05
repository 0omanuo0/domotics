#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""programa de control de riego, con todos los modos"""
__author__  = "Manuel Serrano"
__version__ = "0.4.2a"
__email__ = "manu365manu@gmail.com"


########crear sistema completo de zonas y programacion inicial!!!!

from riego import *
import datetime
import threading
import time
from tkinter import *
from tkinter import ttk, messagebox
import getpass
import pickle
import lectura
blan = True
s = ["pepe",3,"hola"]####
d = [1,1,1]####cargar desde el programa raise NameError('HiThere')
f = [10,2]####
g = [14,15,18]####
h = [True,True,True,True,True,True,False]
a = riego(s, d, f, g, h)
def bucle_principal():###cambiar en app cuando este listo
	while(True):
		a.comprobar()
		print(datetime.datetime.today().weekday())
		time.sleep(0.3)
		lec = lectura.leerParam()
		if(lec[1] == True):
			a.riegoManual()
		elif(lec[2] == True):
			lectura.escribirParam("riego", False)
			lectura.escribirParam("off", False)
			lectura.escribirParam("manual", False)
			quit()

class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.style = ttk.Style()
        self.style.configure("line.TSeparator", background='#222')
        self.raiz.geometry("400x250")

        self.raiz.resizable(0,0)
        self.raiz.title("Sistema domotica "+__version__)
        self.raiz.configure(background='#222')
        self.vis = False
        self.label1 = ttk.Label(self.raiz, text="hola",foreground='#ddd', background='#222')
        self.label2 = ttk.Label(self.raiz, text="Estado: Funcionando...",foreground='#ddd', background='#222')
        self.label3 = ttk.Label(self.raiz, text="by: "+__author__,foreground='#ddd', background='#222')
        #self.ctext2 = ttk.Entry(self.raiz, textvariable="hey", width=30, show="*")
        self.separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL, style="line.TSeparator")
        self.boton1 = ttk.Button(self.raiz, text="manual", padding=(5,5), command=self.Rmanual)
        self.boton2 = ttk.Button(self.raiz, text="Salir", padding=(5,5), command=self.parar)
        self.boton3 = ttk.Button(self.raiz, text="seleccionar", padding=(0,-5), command='''self.esc''')
        self.Lb1 = Listbox(self.raiz)
        self.Lb1.insert(1, "Zona1")
        self.Lb1.insert(2, "Zona2")

        self.label1.place(x=50, y=50)
        self.label2.place(x=195, y=50)
        self.label3.place(x=5, y=230)
        #self.ctext2.place(x=150, y=80)
        self.separ1.place(x=5, y=95, bordermode=OUTSIDE, height=10, width=390)
        self.boton1.place(x=95, y=150)
        self.boton2.place(x=215, y=150)
        self.boton3.place(x=95,y=120, height=25, width=84)
        self.reloj()
        self.raiz.mainloop()

    def reloj(self):
        self.label1.configure(text=time.strftime("%H : %M : %S    Dia: ")+str(datetime.datetime.today().weekday()+1))
        lec = lectura.leerParam()
        if(lec[1] == True):
            self.label2.configure(text="Estado: riego manual")
        elif(lec[2] == True):
            self.label2.configure(text="Estado: off")
        elif(not lec[0] == False):
            self.label2.configure(text="Estado: regando Auto, zon: "+str(lec[0]))
        else:
            self.label2.configure(text="Estado: funcionando...")
        listbo = self.Lb1.curselection()
        try:
            self.boton1.configure(text=("manual",listbo[0]))
        except:
            pass
        self.raiz.after(1000, self.reloj)
    def Rmanual(self):
        try:
        	listbo = self.Lb1.curselection()
        	asdgf = listbo[0]
        	lectura.escribirParam("manual", True)#######lisbo[0]!!!!!!!! poner las zonas
        except:
        	messagebox.showinfo(message="Debe seleccionar una zona", title="error232")
        	print("error232")
        	pass
    def parar(self):
        lectura.escribirParam("riego", False)
        lectura.escribirParam("off", True)
        lectura.escribirParam("manual", False)
        self.raiz.destroy()
def mainApp():
    mi_app = Aplicacion()


th1 = threading.Thread(target=bucle_principal, args=())
th2 = threading.Thread(target=mainApp, args=())
th1.start()
th2.start()
