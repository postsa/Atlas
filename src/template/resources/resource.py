from json import dumps
from ..encoders import ResourceEncoder
from ..resource_resolvers import RefResolver
from .output import Output


class Resource(object):
    def __init__(self, type, name):
        self.type = type
        self.name = name
        self.properties = {}
        self.output = {}

    def template(self):
        return dumps(self, cls=ResourceEncoder, indend=2)

    def get_name_resolver(self):
        return RefResolver(self.name)

    def with_self_ref_output(self, output_name, description=""):
        self.output["{}{}".format(self.name, output_name)] = Output(
            "{}-{}".format(self.name, output_name),
            self.get_name_resolver().resolve(),
            description,
        )
        return self

    def with_attr_output(self, output_name, value_resolver, description=""):
        self.output["{}{}".format(self.name, output_name)] = Output(
            "{}-{}".format(self.name, output_name),
            value_resolver.resolve(),
            description,
        )
        return self

    def get_output_resolver(self):
        if self.output:
            return self.output.get_resolver()
        else:
            raise Exception("No exported value")
