from .resource import Resource


class SecurityGroupIngress(Resource):
    type = "AWS::EC2::SecurityGroupIngress"

    def __init__(self, name, cidr, group_id_resolver, protocol, from_port, to_port):
        super(SecurityGroupIngress, self).__init__(SecurityGroupIngress.type, name)
        self.properties = {
            "CidrIp": cidr,
            "GroupId": group_id_resolver.resolve(),
            "IpProtocol": protocol,
            "FromPort": from_port,
            "ToPort": to_port,
        }
