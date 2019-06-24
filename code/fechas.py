#! usr/bin/python3

import const
import datetime

#Clase para pedir fechas y horas
class TimeHandler(object):

    def __init__(self):
        pass

    def getDayWeek():
        ''' Regresa el dia de la semana, donde 0 es Lunes y 6 es Domingo '''
        return datetime.datetime.today().weekday()

    def getTime():
        ''' Regresa la hora actual'''
        return datetime.datetime.now().time().hour

    def getBloque(self):
        ''' Representa el bloque horario segun el PDF. hay 4 bloques horarios en un dia '''
        hora = self.getTime()

        if (hora == const.horaZero):
            return const.Bloque.BlockA
        if (hora < const.horaPrimer):
            return const.Bloque.BlockA
        
        if (hora == const.horaPrimer):
            return const.Bloque.BlockB
        if (hora < const.horaSegundo):
            return const.Bloque.BlockB
        
        if (hora == const.horaSegundo):
            return const.Bloque.BlockC
        if (hora < const.horaTercer):
            return const.Bloque.BlockC

        if (hora < const.horaCuarto):
            return const.Bloque.BlockD
        
        # Si algo falla
        return const.Bloque.BlockD

    def calculateTask(self):
        ''' Tarea 1 = Medicion. Tarea 2 = Blanco. Tarea 3 = Lavado '''

        # obtenemos dia actual
        # obtenemos el bloque actual
        dia = self.getDayWeek()
        bloque  = self.getBloque()

        #Si es lunes
        if (bloque == const.Bloque.BlockA & dia == 0):
            return const.Tareas.BLANCO
        if (bloque == const.Bloque.BlockA):
            return const.Tareas.LAVAR
        else:
            return const.Tareas.MEDIR
        