#!/usr/bin/env python3
from datetime import datetime
import const

class LogHandler():
	mayor = 1
	minor = 0
	fix   = 0

	def initMsg(self):
		print("Inicio Sistema de sincronizacion de datos")
		print("===========================================")
		print("Iniciado en", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
		self.version()

	def version(self):
		print("Version :", self.mayor,".", self.minor, ".", self.fix)

	def anounceTask(self, tipo):
		''' Escribe en Log el tipo de tarea proxima a realizar'''
		print("-------------------------------------")
		print("LOG => Tarea Calculada :", tipo.name)

