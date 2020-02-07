from .resource import Resource


class Ecr(Resource):
    type = "AWS::ECR::Repository"

    def __init__(self, name, repository_name):
        super(Ecr, self).__init__(Ecr.type, name)
        self.properties = {"RepositoryName": repository_name}
