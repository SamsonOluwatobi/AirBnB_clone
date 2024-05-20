#!/usr/bin/env python3
"""
Module for FileStorage class
"""
# models/__init__.py
import json
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
