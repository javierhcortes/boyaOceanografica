from fechas import TimeHandler
from rutinas import TaskHandler
from iniReader import IniReader

path = "/home/zeusbase/REPOS/boyaOceanografica/code/settings.ini"
section = "DEFAULT"

iniReader = IniReader(path, section)

user = iniReader.getUser()
pasw = iniReader.getPass()
remoteDir = iniReader.getRemoteDir()
localDir = iniReader.getLocalDir()
print ("Datos son: ", user, "-", pasw, remoteDir, localDir)


timeHandler = TimeHandler()
print (timeHandler.calculateTask())

taskHandler = TaskHandler()
taskHandler.archivoFlag_mod