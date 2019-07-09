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
        ## abrir el archivo especificado en path
        ## en modo w.
        file = open("archivoFlag.txt", "w+")

        ## escribe el valor
        file.write(value)

        ## cierra el descriptor
        file.close()
        ## regresa el status
        #return
    def archivoFlag_activar(self):
        return self.archivoFlag_mod('1')
    def archivoFlag_desactivar(self):
        return self.archivoFlag_mod('0')

    ### deberia ir en const.py
    def dir_ifcb(self, tipo):
        switcher = {
            const.subTareas.medicion:'medicion',
            const.subTareas.falsa_medicion:'medicion_falsa',
            const.subTareas.blanco:'blanco',
            const.subTareas.prelavado:'prelavado',
            const.subTareas.lavado:'lavado'
            }
        return switcher.get(tipo, "subTarea invalida")

    ### por implementar
    def executeIFCB(self):
        ''' Ejecutar el archivo ifcb.exe'''
        # import subprocess
        # subprocess.run(["ls", "-l"])
        return
    def waitForFile(self, timeout):
        ''' Esperar los archivos de salida, con timeout definido'''
        # Buscar en la carpeta (definida por sistema) los archivos
        #.adc,.roc,.doi
        #ponerle el time out
        return
    #
    def enviar_configICFB_ftp(self, tipo):
        ''' Actualizar el archivo IFCB.cfg en directorio remoto con 5 disitntos tipos '''
        ''' Med. falsa - confg medicion. blanco. pre lavado- lavado'''
        # toma directorio segun tipo
        directorio_subTarea = self.dir_ifcb(tipo)
        ruta_file = os.path.join(const.ifcb_folder_name, directorio_subTarea, const.ifcb_config_name)

        # Se conecta
        ftp = FTP(ini.getServer())
        ftp.login(user = ini.getUser(), passwd = ini.getPass())
        remoteDir_ifcb = ini.getRemoteDir_ifcb()

        #CWD change working directory
        ftpCommand = 'CWD ' + remoteDir_ifcb
        print( ftp.sendcmd(ftpCommand) )

        #Envia archivo
        with open(ruta_file, 'rb') as fp:
            s = ftp.storbinary('STOR ' + const.ifcb_config_name, fp)
            print ('Cargando de local a remoto', const.ifcb_config_name)
            if str(s).startswith('226'): # comes from ftp status: '226 Transfer complete.'
                print ('OK\n') # print 'OK' if transfer was successful
            else:
                print (s) # if error, print retrbinary's return



    #
    # def transferir_ftp(self):
    #     ''' Transferir archivos generados de cytoBot -> PC104'''
    #     # ejecutar rutina por example2.py modificada
    #     #

    #     h_local_files = [] # create local dir list
    #     h_remote_files = [] # create remote dir list


    #     if os.listdir(h_local) == []:
    #         print ('Directorio local vacio')
    #     else:
    #         print ('construyendo lista de archivos locales...\n')
    #         for file_name in os.listdir(h_local):
    #             h_local_files.append(file_name) # populate local dir list

    #     # Comprobar la existencia de este dir
    #     ftp.sendcmd('CWD /home/javier/REPOS/boyaOceanografica/data/remoto')
    #     print ('Construyendo lista de archivos remotos...\n')
    #     for rfile in ftp.nlst():
    #         # aqui se debe rellenar con condiciones para filtrar archivos (*.roi, *.adc y *.hdr)
    #         #if rfile.endswith('.jpg'): # i need only .jpg files
    #         h_remote_files.append(rfile) # populate remote dir list

    #     # set_remoto = set(h_remote_files)
    #     # set_local = set(h_local_files)

    #     # list_dir = list(set_local - set_remoto)
    #     # #list_dir = list(set_local.symmetric_difference(set_remoto))
    #     # h_diff = sorted(list_dir)
    #     h_diff = sorted(list(set(h_remote_files) - set(h_local_files))) # difference between two lists

    #     for h in h_diff:
    #         print(h)

    #     for h in h_diff:
    #         with open(os.path.join(h_local,h), 'wb') as ftpfile:
    #             s = ftp.retrbinary('RETR ' + h, ftpfile.write) # retrieve file
    #             print ('Cargando archivos de remoto a local', h)
    #             if str(s).startswith('226'): # comes from ftp status: '226 Transfer complete.'
    #                 print ('OK\n') # print 'OK' if transfer was successful
    #             else:
    #                 print (s) # if error, print retrbinary's return

    #     # for h in h_diff:
    #     #     with open(os.path.join(h_local, h), 'r+b') as ftpfile:
    #     #         #s = ftp.retrbinary('RETR ' + h, ftpfile.write) # retrieve file
    #     #         s = ftp.retrbinary('RETR ' + h, lambda s: ftpfile.write(s) and sys.stdout.write('.'))
    #     #         print ('Cargando archivos', h)
    #     #         if str(s).startswith('226'): # comes from ftp status: '226 Transfer complete.'
    #     #             print ('OK\n') # print 'OK' if transfer was successful
    #     #         else:
    #     #             print (s) # if error, print retrbinary's return
    # def transferir1(self):
    #     list_dir = {'texto1', 'texto2'}
    #     for file in list_dir:
    #         with open(os.path.join('/home/javier/REPOS/boyaOceanografica/code', file), 'r+b') as file2transfer:
    #             print(file2transfer.read())


print("solo depuracion")
path = "settings.ini"
section = "PRINCIPAL"

ini = IniReader(path, section)
taskHand = TaskHandler(ini)

print(taskHand.ini.getUser())
#print(taskHand.archivoIFCB_mod(const.subTareas.falsa_medicion))

taskHand.enviar_configICFB_ftp(const.subTareas.prelavado)
# taskHand.transferir_ftp()