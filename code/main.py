from fechas import TimeHandler
from rutinas import TaskHandler
from iniReader import IniReader

path = "/home/zeusbase/REPOS/boyaOceanografica/code/settings.ini"
section = "DEFAULT"

iniReader = IniReader(path, section)
print (iniReader.getUser())#, iniReader.getPass(), iniReader.getRemoteDir(), iniReader.getLocalDir())


timeHandler = TimeHandler()
print (timeHandler.calculateTask())