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

