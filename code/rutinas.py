#!/usr/bin/env python3
import const
import os
import sys
import time
from ftplib import FTP
from iniReader import IniReader


class TaskHandler:
	def __init__(self, iniReader):
		self.ini = iniReader
		self.factorTimeout = 0.01 # Debe ser 1 en terreno

	def archivoFlag_mod(self, value):
		''' Actualizar el valor de flag con valor 1 o 0'''
		with open(const.flagName, 'w+') as fp:
			fp.write(value)

	def archivoFlag_activar(self):
		return self.archivoFlag_mod('1')

	def archivoFlag_desactivar(self):
		return self.archivoFlag_mod('0')

	### por implementar
	def executeIFCB(self):
		''' Ejecutar el archivo ifcb.exe'''
		# import subprocess
		# subprocess.run(["ls", "-l"])
		return

	def enviar_configICFB_ftp(self, tipo):
		''' Actualizar el archivo IFCB.cfg en directorio remoto con 5 tipos '''
		''' Med. falsa - confg medicion. blanco. pre lavado- lavado'''
		# toma directorio segun tipo y construye la ruta relativa a rutinas.py
		directorio_subTarea = const.dir_ifcb(tipo)
		ruta_file = os.path.join(const.ifcb_folder_name, directorio_subTarea, const.ifcb_config_name)

		# print("LOG => Datos login:",self.ini.getUser(), self.ini.getPass())
		# Se conecta
		ftp = FTP(self.ini.getServer())
		login = ftp.login(user=self.ini.getUser(), passwd=self.ini.getPass())
		
		ftp.set_pasv(False)

		# * DEBUG
		# print('LOG => FTP login:', login)
		# print('LOG => Info directorio root ====')
		# print(ftp.retrlines('LIST'))
		# print("================================")

		# Get remote Configuration dir
		remoteDir_ifcb = self.ini.getRemoteDir_ifcb()
 
		#CWD change working directory
		status = ftp.cwd(remoteDir_ifcb)

		# # * DEBUG
		print('LOG => FTP cwd:', status)

		#Envia archivo
		with open(ruta_file, 'rb') as fp:
			s = ftp.storbinary('STOR ' + const.ifcb_config_name, fp)
			print ('LOG => Cargando archivo config IFBC : ', tipo)

			if str(s).startswith('226'): # comes from ftp status: '226 Transfer complete.'
				print ('LOG => Archivo:', tipo, 'cargado exitosamente')
			else:
				print ('LOG => Error en transferencia: ', s) # if error, print storebin's return

		print("LOG => Fin rutina de envio Archivo config FTP")


	def recibir_dataICFB(self):
		#Se conecta
		ftp = FTP(self.ini.getServer())
		login = ftp.login(user = self.ini.getUser(), passwd = self.ini.getPass())
		ftp.set_pasv(False)

		# * DEBUG
		print('LOG => FTP login:', login)
		# print('LOG => Info directorio root ====')
		# print(ftp.retrlines('LIST'))
		# print("================================")

		remoteDir = self.ini.getRemoteDir()
		localDir  = self.ini.getLocalDir()

		h_local_files = [] # create local dir list
		h_remote_files = [] # create remote dir list

		if os.listdir(localDir) == []:
			print ('LOG => Directorio local vacio')
		else:
			print ('LOG => construyendo lista de archivos locales...\n')
			for file_name in os.listdir(localDir):
				h_local_files.append(file_name) # populate local dir list

		#! Comprobar la existencia de este dir remoteDir
		#CWD change working directory
		status = ftp.cwd(remoteDir)

		# * DEBUG
		print('LOG => FTP cwd:', status)

		print ('LOG => Construyendo lista de archivos remotos...\n')
		for rfile in ftp.nlst():
			# aqui se debe rellenar con condiciones para filtrar archivos (*.roi, *.adc y *.hdr)
			if rfile.endswith(('.txt', '.roi', '.adc', '.hdr')): # i need only .jpg files
				h_remote_files.append(rfile) # populate remote dir list

		set_remoto = set(h_remote_files)
		set_local = set(h_local_files)

		## list_dir = list(set_local.symmetric_difference(set_remoto))
		h_diff = sorted(list(set_remoto - set_local)) # difference between two lists

		for h in h_diff:
			with open(os.path.join(localDir, h), 'wb') as ftpfile:
				s = ftp.retrbinary('RETR ' + h, lambda s: ftpfile.write(s) and sys.stdout.write('.')) # retrieve file
				print ('LOG => Cargando archivos resplados de remoto a local: ', h)
				if str(s).startswith('226'): # comes from ftp status: '226 Transfer complete.'
					print ('OK\n') # print 'OK' if transfer was successful
				else:
					print (s) # if error, print retrbinary's return

		print("LOG => Fin rutina de resplado FTP")

	def doRutine(self, tipo):
		print("LOG => Inicio subTareas a realizar:", tipo.name)
		if (tipo == const.Tareas.BLANCO):
			return self.rutinaBlanco()
		elif (tipo == const.Tareas.LAVAR):
			return self.rutinaLavado()
		elif (tipo == const.Tareas.MEDIR):
			return self.rutinaMedicion()

	def rutinaMedicion(self):
		print("LOG => Prox. SubRutina :", TaskHandler.rutinaMedicion.__qualname__)
		self.recibir_dataICFB()
		self.archivoFlag_desactivar()
		self.enviar_configICFB_ftp(const.subTareas.falsa_medicion)
		print("Espera por 5 min")
		time.sleep(5*60*self.factorTimeout)
		self.enviar_configICFB_ftp(const.subTareas.medicion)
		print("Espera por 20 min")
		time.sleep(20*60*self.factorTimeout)
		self.recibir_dataICFB()
		self.archivoFlag_activar()

	def rutinaLavado(self):
		print("LOG => Prox. SubRutina :", TaskHandler.rutinaLavado.__qualname__)
		self.recibir_dataICFB()
		self.archivoFlag_desactivar()
		self.enviar_configICFB_ftp(const.subTareas.prelavado)
		print("Espera por 5 min")
		time.sleep(5*60*self.factorTimeout)
		self.enviar_configICFB_ftp(const.subTareas.lavado)
		print("Espera por 20 min")
		time.sleep(20*60*self.factorTimeout)
		self.recibir_dataICFB()
		self.archivoFlag_activar()

	def rutinaBlanco(self):
		print("LOG => Prox. SubRutina :", TaskHandler.rutinaBlanco.__qualname__)
		self.recibir_dataICFB()
		self.archivoFlag_desactivar()
		self.enviar_configICFB_ftp(const.subTareas.falsa_medicion)
		print("Espera por 5 min")
		time.sleep(5*60*self.factorTimeout)
		self.enviar_configICFB_ftp(const.subTareas.blanco)
		print("Espera por 20 min")
		time.sleep(20*60*self.factorTimeout)
		self.recibir_dataICFB()
		self.archivoFlag_activar()

if __name__ == "__main__":

	print("solo depuracion")
	path = "settings.ini"
	section = "PRINCIPAL"

	ini = IniReader(path, section)
	taskHand = TaskHandler(ini)

	print(taskHand.ini.getUser())
	
	taskHand.enviar_configICFB_ftp(const.subTareas.lavado)
	taskHand.recibir_dataICFB()

