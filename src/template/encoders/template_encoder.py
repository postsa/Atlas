from json import JSONEncoder

from .output_encoder import OutputEncoder
from .resource_encoder import ResourceEncoder
import src.template.resources as resources


class TemplateEncoder(JSONEncoder):
    def default(self, to_encode):
        if isinstance(to_encode, resources.Resource):
            return ResourceEncoder().default(to_encode)
        if isinstance(to_encode, resources.Output):
            return OutputEncoder().default(to_encode)
        else:
            return {"Resources": to_encode.resources, "Outputs": to_encode.outputs}
