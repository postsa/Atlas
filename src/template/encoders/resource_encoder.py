from json import JSONEncoder


class ResourceEncoder(JSONEncoder):
    def default(self, to_encode):
        return {"Type": to_encode.type, "Properties": to_encode.properties}
