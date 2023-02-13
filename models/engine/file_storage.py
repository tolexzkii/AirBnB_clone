#!/usr/bin/python3
import contextlib
import json

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class FileStorage:
    __file_path = "object.json"
    __objects = {}
    class_dict = {
        "BaseModel": BaseModel
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
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
