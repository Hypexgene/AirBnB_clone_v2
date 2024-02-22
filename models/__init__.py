#!/usr/bin/python3
"""
Instantiates a storage object based on the value of the HBNB_TYPE_STORAGE
environmental variable.
"""

from os import getenv
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

storage_type = getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    storage = DBStorage()  
else:
    storage = FileStorage() 

storage.reload()
