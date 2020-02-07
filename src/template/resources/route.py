from .resource import Resource


class Route(Resource):
    type = "AWS::EC2::Route"

    def __init__(
        self,
        name,
        route_table_resolver,
        destination_cidr_block,
        nat_gateway_resolver=None,
        internet_gateway_resolver=None,
    ):
        super(Route, self).__init__(Route.type, name)
        if nat_gateway_resolver:
            self.properties = {
                "NatGatewayId": nat_gateway_resolver.resolve(),
                "RouteTableId": route_table_resolver.resolve(),
                "DestinationCidrBlock": destination_cidr_block,
            }
        elif internet_gateway_resolver:
            self.properties = {
                "GatewayId": internet_gateway_resolver.resolve(),
                "RouteTableId": route_table_resolver.resolve(),
                "DestinationCidrBlock": destination_cidr_block,
            }
