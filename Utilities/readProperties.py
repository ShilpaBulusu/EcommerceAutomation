from configparser import ConfigParser
import pytest
config = ConfigParser()
config.read(".//Configurations/config.ini")

class Config():
    @staticmethod
    def read_config(config_section):
        config_dict = dict()
        for opt in range(len(config.options(config_section))):
            key = config.options(config_section)[opt]
            config_dict.update({key: config.get(config_section, key)})
        return config_dict

