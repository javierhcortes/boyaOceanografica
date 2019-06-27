from enum import Enum, unique

horaZero = 0
horaPrimer = 6
horaSegundo = 12
horaTercer = 18
horaCuarto = 24

@unique 
class Tareas(Enum):
    BLANCO = "blanco"
    LAVAR = "lavar"
    MEDIR = "medir"

@unique 
class Bloque(Enum):
    BlockA = 1
    BlockB = 2
    BlockC = 3
    BlockD = 4

