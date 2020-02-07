from .resource import Resource


class EcsServiceRole(Resource):
    type = "AWS::IAM::Role"

    def __init__(self, name):
        super(EcsServiceRole, self).__init__(EcsServiceRole.type, name)
        self.properties = {
            "AssumeRolePolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Principal": {"Service": ["ecs-tasks.amazonaws.com"]},
                        "Action": ["sts:AssumeRole"],
                    }
                ],
            },
            "Policies": [
                {
                    "PolicyName": "{}Policy".format(name),
                    "PolicyDocument": {
                        "Version": "2012-10-17",
                        "Statement": [
                            {
                                "Effect": "Allow",
                                "Action": [
                                    "ecr:BatchCheckLayerAvailability",
                                    "ecr:BatchGetImage",
                                    "ecr:GetDownloadUrlForLayer",
                                    "ecr:GetAuthorizationToken",
                                ],
                                "Resource": "*",
                            }
                        ],
                    },
                }
            ],
        }
