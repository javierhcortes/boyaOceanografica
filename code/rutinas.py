#!/usr/bin/env python3
import const
import os
import sys
from ftplib import FTP
from iniReader import IniReader

class TaskHandler:
    def __init__(self, iniReader):
        self.ini = iniReader

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
        ''' Actualizar el archivo IFCB.cfg en directorio remoto con 5 disitntos tipos '''
        ''' Med. falsa - confg medicion. blanco. pre lavado- lavado'''
        # toma directorio segun tipo y construye la ruta relativa a rutinas.py
        directorio_subTarea = const.dir_ifcb(tipo)
        ruta_file = os.path.join(const.ifcb_folder_name, directorio_subTarea, const.ifcb_config_name)

        # Se conecta
        ftp = FTP(self.ini.getServer())
        login = ftp.login(user = self.ini.getUser(), passwd = self.ini.getPass())

        # * DEBUG
        print ('FTP login ==>', login)

        # Get remote Configuration dir
        remoteDir_ifcb = self.ini.getRemoteDir_ifcb()

        #CWD change working directory
        ftpCommand = 'CWD ' + remoteDir_ifcb
        status = ftp.sendcmd(ftpCommand)

        # * DEBUG
        print('FTP cwd ==>', status)

        #Envia archivo
        with open(ruta_file, 'rb') as fp:
            s = ftp.storbinary('STOR ' + const.ifcb_config_name, fp)
            print ('Cargando archivo config IFBC : ', tipo)

            if str(s).startswith('226'): # comes from ftp status: '226 Transfer complete.'
                print ('Archivo:', tipo, 'cargado exitosamente')
            else:
                print ('Error en transferencia: ', s) # if error, print storebin's return

    def recibir_dataICFB(self):
        #Se conecta
        ftp = FTP(self.ini.getServer())
        login = ftp.login(user = self.ini.getUser(), passwd = self.ini.getPass())

        # * DEBUG
        print ('FTP login ==>', login)

        remoteDir = self.ini.getRemoteDir()
        localDir  = self.ini.getLocalDir()

        h_local_files = [] # create local dir list
        h_remote_files = [] # create remote dir list

        if os.listdir(localDir) == []:
            print ('Directorio local vacio')
        else:
            print ('construyendo lista de archivos locales...\n')
            for file_name in os.listdir(localDir):
                h_local_files.append(file_name) # populate local dir list

        #! Comprobar la existencia de este dir remoteDir
        #CWD change working directory
        ftpCommand = 'CWD ' + remoteDir
        status = ftp.sendcmd(ftpCommand)

        # * DEBUG
        print('FTP cwd ==>', status)

        print ('Construyendo lista de archivos remotos...\n')
        for rfile in ftp.nlst():
            # aqui se debe rellenar con condiciones para filtrar archivos (*.roi, *.adc y *.hdr)
            #if rfile.endswith('.jpg'): # i need only .jpg files
            h_remote_files.append(rfile) # populate remote dir list

        set_remoto = set(h_remote_files)
        set_local = set(h_local_files)

        ## list_dir = list(set_local.symmetric_difference(set_remoto))
        h_diff = sorted(list(set_remoto - set_local)) # difference between two lists

        for h in h_diff:
            with open(os.path.join(localDir, h), 'wb') as ftpfile:
                s = ftp.retrbinary('RETR ' + h, lambda s: ftpfile.write(s) and sys.stdout.write('.')) # retrieve file
                print ('Cargando archivos resplados de remoto a local: ', h)
                if str(s).startswith('226'): # comes from ftp status: '226 Transfer complete.'
                    print ('OK\n') # print 'OK' if transfer was successful
                else:
                    print (s) # if error, print retrbinary's return

if __name__ == "__main__":

    print("solo depuracion")
    path = "settings.ini"
    section = "PRINCIPAL"

    ini = IniReader(path, section)
    taskHand = TaskHandler(ini)

    print(taskHand.ini.getUser())
    #print(taskHand.archivoIFCB_mod(const.subTareas.falsa_medicion))

    taskHand.enviar_configICFB_ftp(const.subTareas.prelavado)
    taskHand.recibir_dataICFB()

