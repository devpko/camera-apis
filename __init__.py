"""
coding=utf-8

Please get more information from below github repo.

https://github.com/devpko/
"""

import importlib

from .camera import Camera, CAMERA_SETTINGS
from .default import Default
from .basler import Basler

globals().update(importlib.import_module("camapislib").__dict__)
__version__ = '1.0.0'
