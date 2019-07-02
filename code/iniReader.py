#!/usr/bin/python3

import configparser

class iniReader:
    _user = ''
    _pass = ''
    local_directory = ''
    remote_directory = ''
    servidorFTP = ''


    def __init__(self, route):
        self.route = route
        configparser.ConfigParser().read(self.route)
        for (key, value) in config['data.local']
            return


    def getUser(self):
    return

    def getPass(self):
    return

    def getLocalDir(self):
    return

    def getRemoteDir(self):
    return




