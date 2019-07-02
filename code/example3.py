import configparser

Config = configparser.ConfigParser()
Config.read('example.ini')


for (key,value) in Config['PRINCIPAL']:
    print(key, value)
