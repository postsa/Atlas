class OutputResolver(object):
    def __init__(self, output_name):
        self.output_name = output_name

    def resolve(self):
        return {"Fn::ImportValue": self.output_name}
