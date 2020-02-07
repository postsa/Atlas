from .resource import Resource


class EcsService(Resource):
    type = "AWS::ECS::Service"

    def __init__(
        self,
        name,
        cluster_resolver,
        security_group_resolver,
        subnet_resolver,
        task_definition_resolver,
    ):
        super(EcsService, self).__init__(EcsService.type, name)
        self.properties = {
            "Cluster": cluster_resolver.resolve(),
            "LaunchType": "FARGATE",
            "SchedulingStrategy": "REPLICA",
            "DesiredCount": 1,
            "TaskDefinition": task_definition_resolver.resolve(),
            "NetworkConfiguration": {
                "AwsvpcConfiguration": {
                    "AssignPublicIp": "ENABLED",
                    "SecurityGroups": [security_group_resolver.resolve()],
                    "Subnets": [subnet_resolver.resolve()],
                }
            },
        }
