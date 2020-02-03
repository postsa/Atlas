from .resource import Resource


class RouteTable(Resource):
    type = "AWS::EC2::RouteTable"

    def __init__(self, name, vpc_resolver):
        super(RouteTable, self).__init__(RouteTable.type, name)
        self.properties = {"VpcId": vpc_resolver.resolve()}
