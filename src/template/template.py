from json import dumps
from src.template.encoders.template_encoder import TemplateEncoder


class Template(object):
    def __init__(self):
        self.resources = {}
        self.outputs = {}

    def template(self):
        return dumps(self, cls=TemplateEncoder, indent=2)

    def add_resource(self, resource):
        self.resources[resource.name] = resource
        self.add_outputs(resource)

    def add_outputs(self, resource):
        self.outputs.update(resource.output)

    def get_resource(self, resource_name):
        if self.resources[resource_name]:
            return self.resources[resource_name]
        else:
            raise Exception("Resource '{}' not found in template".format(resource_name))
