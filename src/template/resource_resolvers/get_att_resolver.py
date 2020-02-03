class GetAttResolver(object):
    def __init__(self, name, attribute):
        self.name = name
        self.attribute = attribute

    def resolve(self):
        return {"Fn::GetAtt": [self.name, self.attribute]}
