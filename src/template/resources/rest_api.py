from .resource import Resource


class RestApi(Resource):
    type = "AWS::ApiGateway::RestAi"

    def __init__(self, name):
        super(RestApi, self).__init__(RestApi.type, name)
        self.properties = {}
