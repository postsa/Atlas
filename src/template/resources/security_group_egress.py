from .resource import Resource


class SecurityGroupEgress(Resource):
    type = "AWS::EC2::SecurityGroupEgress"

    def __init__(self, name, cidr, group_id_resolver, protocol):
        super(SecurityGroupEgress, self).__init__(SecurityGroupEgress.type, name)
        self.properties = {
            "CidrIp": cidr,
            "GroupId": group_id_resolver.resolve(),
            "IpProtocol": protocol,
        }
