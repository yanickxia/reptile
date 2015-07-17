__author__ = 'Yann.Xia'

import os
from pathlib import Path


class Paths:
    @staticmethod
    def create_paths(location: str):
        paths = os.path.split(location)
        p = Path(paths[0])
        if not p.exists():
            p.mkdir()
            print("create path:", paths[0] + '/')

    @staticmethod
    def is_exist(location):
        return os.path.exists(location)
