#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""programa de control de riego, con todos los modos"""
__author__  = "Manuel Serrano"
__version__ = "0.5.12b"

import sys
import time####
import datetime#### fecha y hora
from gpIO import*
import file_reading

class watering(object):# clase principal riego
	def __init__(self, zon, t, T_ini, pin, dia):
		self.areas     = zon   # nombres de las subzonas
		self.pin_areas = pin   # numero del pin de cada subzona
		self.time      = t     # tiempo de riego de cada subzona
		self.time_init = T_ini # momento de comenzar esta zona en concreto
		self.dias      = dia   # que dias de la semana hay

		self.is_watering = False# variable de control
		self.is_manual   = False

		self.active_area   = 0
		self.watering_time = 0
		self.actual_time   = []
		
		self.gpioAreas = []# variable con los objetos de confiGPIO

		for x in range(len(self.pin_areas)):#crear cada objeto confiGpio para la lista
			self.gpioAreas.append(confiGpio(self.pin_areas[x], 'out'))


		if (len(self.areas) != len(self.time)):##
			print("E1")
		if (len(self.areas) != len(self.pin_areas)):##comprobaciones por si acaso
			print("E2")


	def check(self):#comprobar cada subzona si se inicia usar en el bucle principal !!!falta btn next!!!
		if (self.checkWeekday()):### dia de la semana
			if(not self.is_watering and not self.is_manual):
				if (getTime() == self.time_init):
					self.is_watering = True
					self.active_area = 0
					self.actual_time = getTime('float')
			elif(self.is_watering):
				if(self.time[self.active_area] >= self.watering_time):
					if(len(self.areas) > self.active_area + 1):
						self.active_area += 1
					else:
						self.active_area = 0
						self.is_watering = False
						self.is_manual   = False
				else:
					print("Zon: ", self.active_area)
					self.gpioAreas[self.active_area-1].changeState(False)
					self.gpioAreas[self.active_area  ].changeState(True)
					if(not self.actual_time == getTime('float')):
						self.watering_time =+ 1
						self.actual_time   =+ 1


	def manual(self):
		self.is_manual   = True if not self.is_manual else False
		self.is_watering = True
		self.actual_time = getTime('float')


	def checkWeekday(self):#pequena funcion para comprobar el diaSem, ignorar
		return True if self.dias[datetime.datetime.today().weekday()] else False



def getTime(typeof='degrees'):#pequena funcion para obtener la hora, ignorar
	current_time = [int(time.strftime("%H")), int(time.strftime("%M"))]
	current_time_float = current_time[1] + current_time[0]*60
	return current_time if typeof == 'degrees' else current_time_float if typeof == 'float' else 'E3'

