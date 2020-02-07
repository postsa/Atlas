from pathlib import Path
from os import path

from src.template.template import Template


class ProjectComponent(object):
    def __init__(self, name, project_name, hosted_zone_id, dns_name, *path_dirs):
        self.name = name
        self.project_name = project_name
        self.hosted_zone_id = hosted_zone_id
        self.dns_name = dns_name
        self.template = Template()
        self.directory = path.join(*path_dirs)

    def format_name(self, resource):
        return "{}{}".format(self.name, resource)

    def makedir(self):
        Path(self.directory).mkdir(parents=True, exist_ok=True)

    def write_template(self):
        with open(path.join(self.directory, "template.json"), "w") as f:
            f.write(self.template.template())

    def create_resources(self):
        pass

    def create(self):
        self.makedir()
        self.create_resources()
        self.write_template()

    def get_resource(self, resource):
        return self.template.get_resource(self.format_name(resource))
