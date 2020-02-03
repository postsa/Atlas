from .resource import Resource


class ElasticIp(Resource):
    type = "AWS::EC2::EIP"

    def __init__(self, name, domain):
        super(ElasticIp, self).__init__(ElasticIp.type, name)
        self.properties = {"Domain": domain}
