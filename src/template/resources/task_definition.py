from .resource import Resource


class TaskDefinition(Resource):
    type = "AWS::ECS::TaskDefinition"

    def __init__(self, name, image, execution_role_resolver):
        super(TaskDefinition, self).__init__(TaskDefinition.type, name)
        self.properties = {
            "ContainerDefinitions": [
                {
                    "Interactive": True,
                    "Image": image,
                    "PortMappings": [
                        {"ContainerPort": 80, "HostPort": 80, "Protocol": "tcp"},
                        {"ContainerPort": 22, "HostPort": 22, "Protocol": "tcp"},
                    ],
                    "Name": name,
                }
            ],
            "ExecutionRoleArn": execution_role_resolver.resolve(),
            "Memory": 512,
            "Cpu": "256",
            "RequiresCompatibilities": ["FARGATE"],
            "NetworkMode": "awsvpc",
        }
