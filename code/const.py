from enum import Enum, unique

horaZero = 0
horaPrimer = 6
horaSegundo = 12
horaTercer = 18
horaCuarto = 24

@unique
class Tareas(Enum):
    LAVAR = "lavar"
    MEDIR = "medir"

@unique
class Bloque(Enum):
    BlockA = 1
    BlockB = 2
    BlockC = 3
    BlockD = 4

@unique
class subTareas(Enum):
    medicion = 10
    lavado = 20

flagName = 'archivoFlag.txt'
ifcb_config_name = 'IFCB.cfg'
ifcb_folder_name = 'configIFCB_files'

### lista nombres directorios en configIFCB_files
def dir_ifcb(tipo):
    switcher = {
        subTareas.medicion:       'medicion',
        subTareas.lavado:         'lavado'
        }
    return switcher.get(tipo, "subTarea invalida")
