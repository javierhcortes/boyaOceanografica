#!/usr/bin/env python3
import configparser
import os

class IniReader:

    def __init__(self, path, section):
        self.path = path
        self.section = section
        self.config = self.get_config(path)

    def get_config(self, path):
        'Returns the config object'
        if not os.path.exists(path):
            self.create_config(path)

        config = configparser.ConfigParser()
        config.read(path)
        return config

    def create_config(self, path):
        'Create a config file if miss'
        print("Creando archivo de configuracion...")
        config = configparser.ConfigParser()
        config.add_section('PRINCIPAL')
        config.set('PRINCIPAL', 'local_directory', '/home/user/boyaUdec/data/remoto')
        config.set('PRINCIPAL', 'remote_directory', '/home/user/boyaUdec/data/remoto')

        config.set('PRINCIPAL', 'servidorFTP', 'localhost')
        config.set('PRINCIPAL', 'remote_ifcb_directory', '/home/user/') # directorio en remoto
        config.set('PRINCIPAL', 'user', 'user')
        config.set('PRINCIPAL', 'pass', 'secreto')

        with open(path, "wb") as config_file:
            config.write(config_file)

    def get_setting(self, setting):
        'Print out a setting'

        value = self.config.get(self.section, setting)
        #print(f"*En {self.section} CAMPO {setting} es {value}")
        return value

    def getUser(self):
        return self.get_setting('user')

    def getPass(self):
        return self.get_setting('pass')

    def getLocalDir(self):
        return self.get_setting('local_directory')

    def getRemoteDir(self):
        return self.get_setting('remote_directory')

    def getServer(self):
        return self.get_setting('servidorFTP')

    def getRemoteDir_ifcb(self):
        return self.get_setting('remote_ifcb_directory')



