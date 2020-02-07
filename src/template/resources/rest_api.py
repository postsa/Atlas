from .resource import Resource


class RestApi(Resource):
    type = "AWS::ApiGateway::RestApi"

    def __init__(self, name):
        super(RestApi, self).__init__(RestApi.type, name)
        self.properties = {}
