#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4

import models


class BaseModel:
    def __init__(self, *args, **kwargs):

        if kwargs:
            for key, val in kwargs.items():
                if key == "creatd_at":
                    self.created_at = datetime.strptime(kwargs["created_at"],  "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "update_at":
                    self.updated_at = datetime.strptime(kwargs["update_at"],  "%Y-%m-%dT%H:%M:%S.%f")
                elif key != '__class__':
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
            models.storage.new()

    def __str__(self):
        return f" [{self.__class__.__name__}]{self.id}{self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dic = {"__class__": self.__class__.__name__}
        for k, v in self.__dict__.items():
            dic[k] = v.isoformat() if isinstance(v, (datetime, )) else v
        return dic
