from .resource import Resource


class InternetGateway(Resource):
    type = "AWS::EC2::InternetGateway"

    def __init__(self, name):
        super(InternetGateway, self).__init__(InternetGateway.type, name)
