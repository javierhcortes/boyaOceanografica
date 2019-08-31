#!/usr/bin/env python3

from fechas import TimeHandler
from rutinas import TaskHandler
from iniReader import IniReader
from logger import LogHandler
import const


if __name__ == "__main__":

	#Inicio del logger
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

# if __name__ == "__main__":

# 	#Inicio del logger
# 	logger = LogHandler()
# 	logger.initMsg()

# 	path = "settings.ini"
# 	section = "PRINCIPAL"
# 	iniReader = IniReader(path, section)

# 	#TimeHandler, calcula la tarea en funcion del dia y la hora
# 	timeHandler = TimeHandler()
# 	task = timeHandler.calculateTask()
# 	logger.anounceTask(task)

# 	#TaskHandler realiza las rutinas dependiendo de la tarea calculada anterior%
# 	taskHandler = TaskHandler(iniReader)
# 	#Hace algunas tareas de prueba
# 	taskHandler.archivoFlag_desactivar()
# 	taskHandler.enviar_configICFB_ftp(const.subTareas.medicion)
# 	taskHandler.recibir_dataICFB()