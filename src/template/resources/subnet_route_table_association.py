from .resource import Resource


class SubnetRouteTableAssociation(Resource):
    type = "AWS::EC2::SubnetRouteTableAssociation"

    def __init__(self, name, route_table_resolver, subnet_resolver):
        super(SubnetRouteTableAssociation, self).__init__(
            SubnetRouteTableAssociation.type, name
        )
        self.properties = {
            "RouteTableId": route_table_resolver.resolve(),
            "SubnetId": subnet_resolver.resolve(),
        }
