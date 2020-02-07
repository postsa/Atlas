from src.project.service_component import ServiceComponent
from src.template.resource_resolvers.get_att_resolver import GetAttResolver
from src.template.resources.cluster import Cluster
from src.template.resources.ecs_service import EcsService
from src.template.resources.record_set import RecordSet
from src.template.resources.task_definition import TaskDefinition


class Frontend(ServiceComponent):
    def create_resources(self):
        cluster = Cluster(self.format_name("Cluster"), self.name)
        self.template.add_resource(cluster)
        execution_role = self.bootstrapper.get_resource("ServiceRole")
        task_definition = TaskDefinition(
            self.format_name("TaskDefinition"),
            "nginx",
            execution_role.get_output_resolver(
                "EcrServiceRoleArn"
            ),  # holy magic strings
        )
        self.template.add_resource(task_definition)
        security_group = self.bootstrapper.get_resource("SecurityGroup")
        subnet = self.bootstrapper.get_resource("PublicSubnet")
        service = EcsService(
            self.format_name("EcsService"),
            GetAttResolver(cluster.name, "Arn"),
            security_group.get_output_resolver("ResourceId"),
            subnet.get_output_resolver("Id"),
            task_definition.get_name_resolver(),
        )
        self.template.add_resource(service)
        record_set = RecordSet(
            self.format_name("RecordSet"),
            "{}.{}".format(self.name, self.dns_name),
            self.hosted_zone_id,
            "0.0.0.0",
        )
        self.template.add_resource(record_set)
