from .resource import Resource


class Vpc(Resource):
    type = "AWS::EC2::VPC"

    def __init__(self, name, cidr):
        super(Vpc, self).__init__(Vpc.type, name)
        self.properties = {"CidrBlock": cidr}
