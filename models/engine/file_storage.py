#!/usr/bin/python3
import contextlib
import json

from models.base_model import BaseModel


class FileStorage:
    __file_path = "object.json"
    __objects = {}
    class_dict = {
        "BaseModel": BaseModel
    }

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj:
            key = f" {self.__class__.__name__}.{obj.id}"
            self.__objects = [key]

    def save(self):
        my_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(my_dict, f)

    def reload(self):
        with contextlib.suppress(FileNotFoundError):
            with open(self.__file_path, 'r') as f:
                new_object = json.load(f)
                for key, val in new_object.item():
                    obj = self.class_dict[val['__class__']](**val)
                    self.__objects[key] = obj
