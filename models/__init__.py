#!/usr/bin/python3
"""
    Model init module.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
