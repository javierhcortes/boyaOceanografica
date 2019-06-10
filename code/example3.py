import configparser

config = configparser.ConfigParser()
config.read('example.ini')


for (key, value) in config['prueba.local']:  
    print(key, value)
