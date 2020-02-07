from .resource import Resource


class Cluster(Resource):
    type = "AWS::ECS::Cluster"

    def __init__(self, name, cluster_name):
        super(Cluster, self).__init__(Cluster.type, name)
        self.properties = {"ClusterName": cluster_name}
