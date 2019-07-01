import configparser

config = configparser.ConfigParser()
config.read('example.ini')


for key in config['prueba.local']:  
    print(key)
