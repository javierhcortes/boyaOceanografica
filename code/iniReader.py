#!/usr/bin/python3
import configparser
import os

class IniReader:
    # _config = []
    # _section = ''
    # _path = ''

    def __init__(self, path, section):
        self.path = path
        self.section = section
        self.config = self.get_config(path)

    def get_config(self, path):
        'Returns the config object'
        if not os.path.exists(path):
            create_config(path)

        config = configparser.ConfigParser()# configParser.configParser()
        config.read(path)
        return config

    def create_config(self, path):
        'Create a config file if miss'

        config = configParser.configParser()
        config.add_section('DEFAULT')
        config.set('DEFAULT', 'local_directory', '/home/user/boyaUdec/data/remoto')
        config.set('DEFAULT', 'remote_directory', '/home/user/boyaUdec/data/remoto')
        config.set('DEFAULT', 'servidorFTP', 'localhost')
        config.set('DEFAULT', 'user', 'user')
        config.set('DEFAULT', 'pass', 'secreto')

        with open(path, "wb") as config_file:
            config.write(config_file)

    def get_setting(self, setting): #path, section, setting):
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






