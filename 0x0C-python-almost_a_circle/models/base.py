#!/usr/bin/python3
'''This is a module'''

import json
import csv


class Base:
    '''This is a class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''This is a method'''
        self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''This is a method'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''This is a method'''
        jsArray = []
        if list_objs is not None and list_objs:
            for obj in list_objs:
                jsArray.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(jsArray))

    @staticmethod
    def from_json_string(json_string):
        '''This is a method'''
        if json is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''This is a method'''
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''This is a method'''
        try:
            with open(cls.__name__ + ".json", encoding="utf-8") as f:
                jsList = cls.from_json_string(f.read())
                listOfInstances = []
                for singleDictionary in jsList:
                    newDictionary = {}
                    for key, value in singleDictionary.items():
                        newDictionary[key] = value
                    listOfInstances.append(cls.create(**newDictionary))
                return listOfInstances
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''This is a method'''
        with open(cls.__name__ + ".csv", "w", encoding="utf-8") as f:
            if list_objs is not None and list_objs:
                if cls.__name__ == "Rectangle":
                    head = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    head = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=head)
                writer.writeheader()
                for row in list_objs:
                    writer.writerow(row.to_dictionary())
            else:
                f.write("[]")

    @classmethod
    def load_from_file_csv(cls):
        '''This is a method'''
        try:
            with open(cls.__name__ + ".csv", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                delist = []
                for derow in reader:
                    for key, value in derow.items():
                        derow[key] = int(value)
                    delist.append(cls.create(**derow))
            return delist
        except Exception:
            return []
