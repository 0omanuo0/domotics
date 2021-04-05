import sys
import time####
import datetime#### fecha y hora
#import RPi.GPIO as GPIO

class RegulacionTemp(object):
	def __init__(self):
		self.tempZonas = []#temperatura actual
		self.tempSelecZ = []#temperatura que quieres en la zona
		#self.nivelCompZon = []#
		self.Zonas = []#nombre subzonas
		'''self.tempFancE#salida
		self.tempFancR#retorno
		self.tempExtAmb'''
		self.tempCondens = 0#temperatura a la que esta la salida de gas
		'''self.humedadEx
		self.humedadIn'''
		self.modo = 0#0 frio, 1 calor, 2 ventilador
		self.nivelPfanc=0#1,2,3,0
		self.nivelUsFanc = []#1,2,3, auto = 4, eco = 5, off = 0
		self.Power = False #variable control del motor on/off
		self.PowerTotal = False#variable control on/off
		self.BufferErr = []
		self.pinFancoil = []#1,2,3,on ESTE SENTIDO
		self.pinComp = []
	def sistemaG(self, estado):
		if(estado == True):
			print("arranca")
			pass#arrancar
		else:
			print("para")
			pass
	def fancCoil(self, nv):
		self.nivelPfanc = nv
		if(self.nivelPfanc == 1):
			print("FancNv1")
			self.Power = True
			pass#arrancar
		elif(self.nivelPfanc == 2):
			print("FancNv2")
			self.Power = True
			pass#arrancar
		elif(self.nivelPfanc == 3):
			print("FancNv3")
			self.Power = True
			pass#arrancar
		elif(self.nivelPfanc == 0):
			print("FancOff")
			self.Power = False
			pass#arrancar
		else:
			self.Power = False
			print("E4")
			self.BufferErr.append("E4")
			self.comprobar()
			pass
	'''def calcularTemp(self, temp):#calculo proporcional/integral
		pass
		self.nivelPfanc = variable yo que se
		self.fancCoil()
	def eco(self):#calculo proporcional/integral mas suave y reducir mucho el motor y demas
		pass
		self.nivelPfanc = variable yo que se
		self.fancCoil()'''
	def UsuarioVent(self, nv):
		self.nivelUsFanc = nv
		if(self.nivelUsFanc == 1):
			print("FancNv1")
			self.Power = True
			fancCoil(1)
			pass#arrancar
		elif(self.nivelUsFanc == 2):
			print("FancNv2")
			self.Power = True
			fancCoil(2)
			pass#arrancar
		elif(self.nivelUsFanc == 3):
			print("FancNv3")
			self.Power = True
			self.fancCoil(3)
			pass#arrancar
		elif(self.nivelUsFanc == 0):
			print("FancOff")
			self.Power = False
			pass#arrancar
		else:
			self.Power = False
			print("E5")
			self.BufferErr.append("E5")
			self.comprobar()
			pass
	def comprobar(self):#guardar temperaturas de cada sitio
		if(self.BufferErr.len() == 3):
			print(self.BufferErr[self.BufferErr.len()-1])
			self.parar()
			return 0
		else:
			if(self.tempCondens > 15):#ya mirare
				self.BufferErr.append("E3")
				self.comprobar()
			self.UsuarioVent()

a = RegulacionTemp()
a.UsuarioVent(3)