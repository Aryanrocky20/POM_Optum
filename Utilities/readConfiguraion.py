import os
from configparser import ConfigParser


class ReadProperties:

    def readConfiguration(section, key):
        cfg = ConfigParser()
        file_path = os.path.relpath('.\\Configuration\\config.ini')
        cfg.read(file_path)

        return cfg.get(section, key)


    def readLocators(section, key):
        cfg = ConfigParser()
        file_path = os.path.relpath('.\\Configuration\\locators.ini')
        cfg.read(file_path)

        data = cfg.get(section, key)
        return data
