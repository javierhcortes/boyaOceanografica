#! usr/bin/python3

import datetime

#Clase para pedir fechas y horas
class TimeHandler(object):

    horaZero = 0;
    horaPrimer = 6;
    horaSegundo = 12;
    horaTercer = 18;
    horaCuarto = 24;

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

        if (hora == self.horaZero):
            return 1
        if (hora < self.horaPrimer):
            return 1
        
        if (hora == self.horaPrimer):
            return 2
        if (hora < self.horaSegundo):
            return 2
        
        if (hora == self.horaSegundo):
            return 3
        if (hora < self.horaTercer):
            return 3

        if (hora < self.horaCuarto):
            return 4
        
        # Si algo falla
        return 4

    def calculateTask(self):
        ''' Tarea 1 = Medicion. Tarea 2 = Blanco. Tarea 3 = Lavado '''

        # obtenemos dia actual
        # obtenemos el bloque actual
        dia = self.getDayWeek()
        bloque  = self.getBloque()

        if (bloque == 1 & dia == 0):
            return 'Blanco'
        if (bloque == 1):
            return 'Lavado'
        else:
            return 'Medicion'
        