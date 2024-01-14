#!/usr/bin/python3
"""
This module shall contain the BaseModel class
"""

import uuid
from datetime import datetime
import models
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from os import getenv

temp = "%Y-%m-%dT%H:%M:%S.%f"

Base = declarative_base()

class BaseModel:
    """This is the BaseModel class
    Attributes:
        id (str): This represent the id
        created_at (datetime): This represent the created at
        updated_at (datetime): This represent the updated at
    """
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())
    
    def __init__(self, *args, **kwargs):
        """this shall init Base MOdel"""
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        setattr(self, k, datetime.strptime(v, temp))
                    else:
                        setattr(self, k, v)
            if kwargs.get("id") is None:
                setattr(self, "id", str(uuid.uuid4()))
            if kwargs.get("created_at") is None:
                setattr(self, "created_at", datetime.now())
            if kwargs.get("updated_at") is None:
                setattr(self, "updated_at", datetime.now())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """This shall return the string representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
    
    def save(self):
        """This shall save the instance"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """This shall return the dictionary representation"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict
    
    def delete(self):
        """This shall delete the instance"""
        models.storage.delete(self)
