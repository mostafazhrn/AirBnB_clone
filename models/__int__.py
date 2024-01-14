#!/usr/bin/python3
"""This shall init storage of file storage"""
from models.engine.file_storage import Filestorage


storage = Filestorage()
storage.reload()
