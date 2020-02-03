from os import path
from pathlib import Path
import pickle


class FileSystemDb(object):
    def __init__(self, *dir):
        self.dir = path.join(*dir)
        self.file = path.join(*dir, "atlas")
        if not self.persisted():
            Path(self.dir).mkdir(parents=True, exist_ok=True)

    def save(self, atlas):
        with open(self.file, "wb") as f:
            pickle.dump(atlas, f)

    def persisted(self):
        return path.isfile(self.file)

    def load(self):
        if self.persisted:
            with open(self.file, "rb") as f:
                return pickle.load(f)
        else:
            raise Exception("Cannot load, no previous version exists")
