from .resource import Resource


class Subnet(Resource):
    type = "AWS::EC2::Subnet"

    def __init__(self, name, cidr, vpc_resolver, map_public_ip_on_launch):
        super(Subnet, self).__init__(Subnet.type, name)
        self.properties = {
            "CidrBlock": cidr,
            "VpcId": vpc_resolver.resolve(),
            "MapPublicIpOnLaunch": map_public_ip_on_launch,
        }
