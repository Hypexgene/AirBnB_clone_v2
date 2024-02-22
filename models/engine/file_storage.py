#!/usr/bin/python3
"""The module that defines a class to manage file storage for hbnb clone"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of all objects or objects of a specific class.

        Args:
            cls (class, optional): The class type to filter objects. Defaults to None.

        Returns:
            dict: A dictionary of objects.
        """
        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.

        Args:
            obj (BaseModel): The object to add.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes the storage dictionary to a JSON file."""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """
        Deserializes the JSON file into the storage dictionary.
        """
        if os.path.isfile(self.__file_path):
            try:
                with open(self.__file_path, "r", encoding="utf-8") as f:
                    obj_dict = json.load(f)
                    self.__objects = {k: eval(v["__class__"])(**v) for k, v in obj_dict.items()}
            except Exception as e:
                print(f"Error reloading data: {e}")

    def delete(self, obj=None):
        """
        Deletes the given object from the storage dictionary.

        Args:
            obj (BaseModel, optional): The object to delete. Defaults to None.
        """
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects.pop(key, None)

    def close(self):
        """Reloads the storage."""
        self.reload()
