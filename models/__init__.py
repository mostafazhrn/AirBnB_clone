#!/usr/bin/python3
"""THis shall init the model and model.storage"""
from models.engine.file_storage import Filestorage


storage = Filestorage()
storage.reload()
