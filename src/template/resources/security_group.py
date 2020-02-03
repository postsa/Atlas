from .resource import Resource


class SecurityGroup(Resource):
    type = "AWS::EC2::SecurityGroup"

    def __init__(self, name, vpc_resolver, group_description, group_name):
        super(SecurityGroup, self).__init__(SecurityGroup.type, name)
        self.properties = {
            "VpcId": vpc_resolver.resolve(),
            "GroupDescription": group_description,
            "GroupName": group_name,
        }
