from json import JSONEncoder
from src.template.resources.resource import Resource
from src.template.resources.output import Output
from .output_encoder import OutputEncoder
from .resource_encoder import ResourceEncoder


class TemplateEncoder(JSONEncoder):
    def default(self, to_encode):
        if isinstance(to_encode, Resource):
            return ResourceEncoder().default(to_encode)
        if isinstance(to_encode, Output):
            return OutputEncoder().default(to_encode)
        else:
            return {"Resources": to_encode.resources, "Outputs": to_encode.outputs}
