from .resource import Resource


class Route(Resource):
    type = "AWS::EC2::Route"

    def __init__(
        self, name, nat_gateway_resolver, route_table_resolver, destination_cidr_block
    ):
        super(Route, self).__init__(Route.type, name)
        self.properties = {
            "NatGatewayId": nat_gateway_resolver.resolve(),
            "RouteTableId": route_table_resolver.resolve(),
            "DestinationCidrBlock": destination_cidr_block,
        }
