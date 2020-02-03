from .resource import Resource


class VpcGatewayAttachment(Resource):
    type = "AWS::EC2::VPCGatewayAttachment"

    def __init__(self, name, internet_gateway_resolver, vpc_resolver):
        super(VpcGatewayAttachment, self).__init__(VpcGatewayAttachment.type, name)
        self.properties = {
            "VpcId": vpc_resolver.resolve(),
            "InternetGatewayId": internet_gateway_resolver.resolve(),
        }
