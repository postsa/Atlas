from src.template.resource_resolvers.output_resolver import OutputResolver


class Output(object):
    def __init__(self, name, value, description):
        self.name = name
        self.value = value
        self.description = description

    def get_resolver(self):
        return OutputResolver(self.name)
