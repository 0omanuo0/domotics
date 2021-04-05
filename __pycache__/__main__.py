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

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""programa de control de riego, con todos los modos"""
__author__  = "Manuel Serrano"
__version__ = "0.5.12b"

import sys
import time####
import datetime#### fecha y hora
from gpIO import*
import lectura

class riego(object):# clase principal riego
    def __init__(self, zon, t, T_ini, pin, dia):
        self.lManual = confiGpio(20, 'out')
        self.bManual = confiGpio(16, 'in')
        self.zonas = zon# nombres de las subzonas
        self.pinZonas = pin# numero del pin de cada subzona
        self.ZonaAct = 0
        self.tiempo = t# tiempo de riego de cada subzona
        self.T_inicio = T_ini# momento de comenzar esta zona en concreto
        self.riego_inic = False# variable de control
        self.nZonas = len(self.zonas)# variable de control
        self.gpioZonas = []# variable con los objetos de confiGPIO
        self.zonas_ini = []# a que hora comienza cada subzona
        self.acaba_zon = []# a que hora acaba esta zona
        self.NivelTanqAgua = 0
        self.dias = dia# que dias de la semana hay
        if (len(self.zonas) != len(self.tiempo)):##
            print("E1")
        if (len(self.zonas) != len(self.pinZonas)):##comprobaciones por si acaso
            print("E2")

        i = 0######no tocar, no se como va xddd
        lista = []
        while(len(self.tiempo) + 1 > i):
            y = self.T_inicio[1]
            for x in range(i):
                y = y + self.tiempo[x]
            lista.append(y)
            i += 1
        for x in range(len(lista)):
            self.zonas_ini.append([self.T_inicio[0],lista[x]])
            while(self.zonas_ini[x][1] >= 60):
                    self.zonas_ini[x][1] = self.zonas_ini[x][1] - 60
                    self.zonas_ini[x][0] = self.zonas_ini[x][0] + 1
        self.acaba_zon = self.zonas_ini[len(self.zonas_ini)-1]#hasta aqui xddd
        self.zonas_ini.pop()
        print(self.zonas_ini, " - ", self.acaba_zon)

        for x in range(len(self.pinZonas)):#crear cada objeto confiGpio para la lista
            exec("sdg{} = confiGpio(self.pinZonas[{}], 'out')".format(x, x))
            exec("self.gpioZonas.append(sdg{})".format(x))
            exec("self.gpioZonas[{}].llmamar_pin(True)".format(x))
            exec("self.gpioZonas[{}].llmamar_pin(False)".format(x))
        #print(self.zonas_ini)

    def riegoManual(self):#copia y pega del comprobar !!!falta btn next!!!
        paraZonaM = False
        ZonaActM = 0
        T_inicioM = obtener_hora()
        zonas_iniM = []
        acaba_zonM = []
        i = 0######no tocar, no se como va xddd
        lista = []
        while(len(self.tiempo) + 1 > i):
            y = T_inicioM[1]
            for x in range(i):
                y = y + self.tiempo[x]
            lista.append(y)
            i += 1
        for x in range(len(lista)):
            zonas_iniM.append([T_inicioM[0],lista[x]])
            while(zonas_iniM[x][1] >= 60):
                    zonas_iniM[x][1] = zonas_iniM[x][1] - 60
                    zonas_iniM[x][0] = zonas_iniM[x][0] + 1
        acaba_zonM = zonas_iniM[len(zonas_iniM)-1]#hasta aqui xddd
        zonas_iniM.pop()
        print(zonas_iniM, " - ", acaba_zonM)
        lec = lectura.leerParam()
        while(paraZonaM == False and lec[1] != False):#bucle principal modo manual, anula temp el normal, si manual = false parar
            lec = lectura.leerParam()
            if(obtener_hora() in zonas_iniM):
                self.lManual.llmamar_pin(True)
                ZonaActM = zonas_iniM.index(obtener_hora())
                print("Zon: ", ZonaActM)
                exec("self.gpioZonas[{}].llmamar_pin(False)".format(ZonaActM-1))
                exec("self.gpioZonas[{}].llmamar_pin(True)".format(ZonaActM))
            elif(obtener_hora() == acaba_zonM):
                for x in range(len(self.pinZonas)):
                    exec("self.gpioZonas[{}].llmamar_pin(False)".format(x))
                print("c  acabo")
                print("nop")#######
                paraZonaM = True
            else:
                print("Zon: ", ZonaActM)
                exec("self.gpioZonas[{}].llmamar_pin(False)".format(ZonaActM-1))
                exec("self.gpioZonas[{}].llmamar_pin(True)".format(ZonaActM))
            time.sleep(0.3)
            if(lec[2] == True):
                print("hola")
                lectura.escribirParam("riego", False)
                lectura.escribirParam("off", False)
                lectura.escribirParam("manual",False)
                quit()
                
        self.lManual.llmamar_pin(False)
        lectura.escribirParam("manual", False)

    def comprobar(self):#comprobar cada subzona si se inicia usar en el bucle principal !!!falta btn next!!!
        if (self.comprobarDSemana() == True):### dia de la semana
            if(self.riego_inic == False):
                if (obtener_hora() in self.zonas_ini and lectura.leerParam()[5] == True):####### hora
                    self.riego_inic = True
                    print("inicio")
            else:
                if(obtener_hora() in self.zonas_ini):
                    print("hola ")
                    self.ZonaAct = self.zonas_ini.index(obtener_hora())
                    print("Zon: ", self.ZonaAct)
                    exec("self.gpioZonas[{}].llmamar_pin(False)".format(self.ZonaAct-1))
                    lectura.escribirParam("riego", self.ZonaAct)
                elif(obtener_hora() == self.acaba_zon):
                    self.riego_inic = False
                    for x in range(len(self.pinZonas)):
                        exec("self.gpioZonas[{}].llmamar_pin(False)".format(x))
                    print("c  acabo")
                    lectura.escribirParam("riego", False)
                    print("nop")#######
                else:
                    print("Zon: ", self.ZonaAct)
                    exec("self.gpioZonas[{}].llmamar_pin(False)".format(self.ZonaAct-1))
                    exec("self.gpioZonas[{}].llmamar_pin(True)".format(self.ZonaAct))
                    lectura.escribirParam("riego", self.ZonaAct)
                if(lectura.leerParam()[5] == False):
                    self.riego_inic = False
        else:
            print("nop, sem")###
        if self.bManual.leer_pin() == True:#cambiar a GPIO.HIGH
            print("Manual")
            self.riegoManual()

    def comprobarDSemana(self):#pequena funcion para comprobar el diaSem, ignorar
        if (self.dias[datetime.datetime.today().weekday()] == True):
            return True
        else:
            return False

    '''def autoHumedadTemperatura(self):####mirar en un futuro####
        if (----humedad---- < 10 and obtener_hora[0] > 22 and obtener_hora[0] < 8):
            pass
        else if (----temperatura---- > 40 and obtener_hora[0] > 22 and obtener_hora[0] < 8):
            pass# momento mas alto de temp del dia(mirar en un futuro)'''

'''def bucle_principal(bu, z, t, ti) # asi es como deberia de ser!!!
    b = bu
    exec("{} = riego({},{},{})".format(b,z,t,ti))'''

def obtener_hora():#pequena funcion para obtener la hora, ignorar
    h = [0,0]
    h[0] = int(time.strftime("%H"))
    h[1] = int(time.strftime("%M"))
    return(h)

