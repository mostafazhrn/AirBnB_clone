#!/usr/bin/python3
"""THis shall init the model and model.storage"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
