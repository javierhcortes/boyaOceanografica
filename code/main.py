from fechas import TimeHandler
from rutinas import TaskHandler
from iniReader import IniReader

path = "settings.ini"
section = "PRINCIPAL"

iniReader = IniReader(path, section)

user = iniReader.getUser()
pasw = iniReader.getPass()
remoteDir = iniReader.getRemoteDir()
localDir = iniReader.getLocalDir()
print ("Datos son: ", user, "-", pasw, remoteDir, localDir)


timeHandler = TimeHandler()
print (timeHandler.calculateTask())


taskHandler = TaskHandler(iniReader)
taskHandler.archivoFlag_activar()