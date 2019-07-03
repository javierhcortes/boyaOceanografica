#!/usr/bin/python3
import configparser
import os


def get_config(path):
    """
    Returns the config object
    """
    if not os.path.exists(path):
        create_config(path)

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


path = "settings.ini"

l1 = get_setting(path,'DEFAULT', 'local_directory')

# Config = configparser.ConfigParser()
# Config.read('example.ini')

# dict = {}

# for key in Config['PRINCIPAL']:
#     print(key)


