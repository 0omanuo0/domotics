#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""control pines GPIO para el sistema general"""
__author__  = "Manuel Serrano"
__version__ = "1.1.3b(non GPIO pin implemented version)"

import sys


#import RPi.GPIO as GPIO
class confiGpio(object):

	def __init__(self, pin, modo):#, modo, tipo
		self.GPIOPin = pin# saber que pin es
		self.estadoPin = False# variable controlGPIO.IN, pull_up_down=GPIO.PUD_DOWN
		self.mod = modo
		#GPIO.setmode(GPIO.BCM)# modificar el parametro tipo !!!!no tocar!!!!
		if self.mod == 'out':# tipo de pin(salida o entrada)
			#GPIO.setup(self.GPIOPin, GPIO.OUT)
			print(self.GPIOPin, self.mod)
		elif self.mod == 'in':
			#GPIO.setup(self.GPIOPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
			print(self.GPIOPin, self.mod)
			self.changeState(True)
			self.changeState(False)
		

	def changeState(self, llamarPin):
		if (llamarPin == True):#poner en HIGH/LOW el pin
			self.estadoPin = True
			#GPIO.output(self.GPIOPin,GPIO.LOW)
			print("ini", self.GPIOPin)
		else:
			self.estadoPin = False
			#GPIO.output(self.GPIOPin,GPIO.HIGH)
			print("par", self.GPIOPin)

	def readPin(self):
		#return GPIO.input(self.GPIOPin)
		return False
