#!/usr/bin/env python3

from fechas import TimeHandler
from rutinas import TaskHandler
from iniReader import IniReader
import const


if __name__ == "__main__":
    path = "settings.ini"
    section = "PRINCIPAL"
    iniReader = IniReader(path, section)

    # timeHandler = TimeHandler()
    # print (timeHandler.calculateTask())

    taskHandler = TaskHandler(iniReader)
    taskHandler.archivoFlag_desactivar()

    taskHandler.enviar_configICFB_ftp(const.subTareas.prelavado)
    taskHandler.recibir_dataICFB()