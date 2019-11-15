#!/usr/bin/env python3

from fechas import TimeHandler
from rutinas import TaskHandler
from iniReader import IniReader
from logger import LogHandler
import const
import time
import subprocess

#import datetime

if __name__ == "__main__":

	#Inicio del logger
	print("LOG =>Wait 30 segundos")
	time.sleep(30)
	logger = LogHandler()
	logger.initMsg()

	path = "settings.ini"
	section = "PRINCIPAL"
	iniReader = IniReader(path, section)

	#TimeHandler, calcula la tarea en funcion del dia y la hora
	timeHandler = TimeHandler()

	task = timeHandler.calculateTask()
	logger.anounceTask(task)

	#TaskHandler realiza las rutinas dependiendo de la tarea calculada anterior%
	taskHandler = TaskHandler(iniReader)
	taskHandler.doRutine(task)
	
	print("LOG => Wait 5min ")
	time.sleep(60*5)
	#Se demora un minuto en apagarse
	subprocess.call(["shutdown", "/s"])


# if __name__ == "__main__pruebas":

# 	#Inicio del logger
# 	time.sleep(30)
# 	logger = LogHandler()
# 	logger.initMsg()

# 	path = "settings.ini"
# 	section = "PRINCIPAL"
# 	iniReader = IniReader(path, section)

# 	#TimeHandler, calcula la tarea en funcion del dia y la hora
# 	timeHandler = TimeHandler()
# 	task = timeHandler.calculateTask()
# #Calculo de tiempo para tarea custom
# horaActual = datetime.datetime.now().time().hour
# minActual = datetime.datetime.now().time().minute
# HoraPonderadaActual = horaActual*60 + minActual

# horaMargen = 780 # 13:00am
# if (HoraPonderadaActual < horaMargen):
# 	print("LOG =>inicio Pruebas de MEDICION CUSTOM1...")
# 	taskHandler.rutinaMedicion()
# 	print("LOG =>fin Pruebas de MEDICION...")
# elif (HoraPonderadaActual >= horaMargen):
# 	print("LOG =>inicio Pruebas de LAVADO CUSTOM2...")
# 	taskHandler.rutinaLavado()
# 	print("LOG =>fin Pruebas de LAVADO...")
# else:
# 	print("LOG =>inicio Pruebas de LAVADO CUSTOM3...")
# 	taskHandler.rutinaLavado()
# 	print("LOG =>fin Pruebas de LAVADO...")

# import subprocess
# subprocess.call(["shutdown", "/s"])
