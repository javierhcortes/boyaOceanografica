class TaskHandler:

    def archivoFlag_activar(self):
        return self.archivoFlag_mod('1')
    def archivoFlag_desactivar(self):
        return self.archivoFlag_mod('0')

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

    def archivoIFCB_mod(self, tipo):
        ''' Actualizar el archivo IFCB.cfg con 5 disitntos tipos '''
        ''' Med. falsa - confg medicion. blanco. pre lavado- lavado'''
        ## Busca dir de archivo IFCB.cfg a actualzar
        ## BUSCA dir con todos los tipos de archivos ifcb.cfg
        # copia el archivo elegido en el directorio
        # regresa el valor

        return

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

    def transferir_ftp(self):
        ''' Transferir archivos generados de cytoBot -> PC104'''
        # ejecutar rutina por example2.py modificada
        #
        return


print("solo depuracion")

taskHand = TaskHandler()


taskHand.archivoFlag_desactivar()