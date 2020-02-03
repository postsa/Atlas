from pathlib import Path
from os import path

from src.template.template import Template


class ProjectComponent(object):
    def __init__(self, name, *path_dirs):
        self.name = name
        self.template = Template()
        self.directory = path.join(*path_dirs)

    def format_name(self, resource):
        return "{}{}".format(self.name, resource)

    def makedir(self):
        Path(self.directory).mkdir(parents=True, exist_ok=True)

    def write_template(self):
        with open(path.join(self.directory, "bootstrap.json"), "w") as f:
            f.write(self.template.template())

    def create_resources(self):
        pass

    def create(self):
        self.makedir()
        self.create_resources()
        self.write_template()
