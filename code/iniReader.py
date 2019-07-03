#!/usr/bin/python3
import configparser
import os

class iniReader:

    path = "settings.ini"
    section = "DEFAULT"

    def __init__(self, path):
        """
        Returns the config object
        """
        # if not os.path.exists(path):
        #     create_config(path)

        config = configparser.ConfigParser()
        config.read(path)
        return config

    def get_setting(path, section, setting):
        """
        Print out a setting
        """
        config = get_config(path)
        value = config.get(section, setting)
        print(f'*En {section} CAMPO {setting} es {value}')
        return value

    def getUser(self):
        return user = get_setting(path, section, 'user')

    def getPass(self):
        return get_setting(path, section, 'pass')

    def getLocalDir(self):
        return get_setting(path, section, 'local_directory')

    def getRemoteDir(self):
        return get_setting(path, section, 'remote_directory')

    def getServer(self):
        return get_setting(path, section, 'servidorFTP')






