import json
import jsonschema
from jsonschema import validate

class Validate_JSON:
    
    def __init__(self, schemej, file_path):
        self.schemej = schemej
        self.__file_path = file_path

    @property
    def schemej(self):
        return self.__schemej

    @schemej.setter
    def schemej(self, schemej):
        if not isinstance(schemej, object):
            raise ValueError('There is no object arg')

        self.__schemej = schemej

    @property
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self, file_path):
        if not isinstance(file_path, str):
            raise ValueError('There is no str arg')

        self.__file_path = file_path

    def validate(self):
        with open(self.file_path) as datas:
            data = json.load(datas)
        try:
            jsonschema.validate(data, self.schemej)
            return data
        except jsonschema.ValidationError as exp:
            raise Exception(f'JSON data error, details: {exp}')