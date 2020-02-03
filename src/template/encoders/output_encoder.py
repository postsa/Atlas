from json import JSONEncoder


class OutputEncoder(JSONEncoder):
    def default(self, to_encode):
        return {
            "Description": to_encode.description,
            "Value": to_encode.value,
            "Export": {"Name": to_encode.name},
        }
