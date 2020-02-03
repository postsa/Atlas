from .resource import Resource


class NatGateway(Resource):
    type = "AWS::EC2::NatGateway"

    def __init__(self, name, allocation_id_resolver, public_subnet_resolver):
        super(NatGateway, self).__init__(NatGateway.type, name)
        self.properties = {
            "AllocationId": allocation_id_resolver.resolve(),
            "SubnetId": public_subnet_resolver.resolve(),
        }
