class RefResolver(object):
    def __init__(self, name):
        self.name = name

    def resolve(self):
        return {"Ref": self.name}
