from src.project.service_component import ServiceComponent
from src.template.resource_resolvers.get_att_resolver import GetAttResolver
from src.template.resources.cluster import Cluster
from src.template.resources.ecs_service import EcsService
from src.template.resources.record_set import RecordSet
from src.template.resources.task_definition import TaskDefinition

from os import path, environ


class Frontend(ServiceComponent):
    def __init__(
        self, name, project_name, hosted_zone_id, dns_name, bootstrapper, *path_dirs
    ):
        super(Frontend, self).__init__(
            name, project_name, hosted_zone_id, dns_name, bootstrapper, *path_dirs
        )
        self.ecr_uri = "{}.dkr.ecr.us-west-2.amazonaws.com/{}/images".format(
            environ["AWS_ACCOUNT_ID"], self.project_name.lower()
        )
        self.image_name = "{}".format(self.ecr_uri)

    def create_resources(self):
        cluster = Cluster(self.format_name("Cluster"), self.name)
        self.template.add_resource(cluster)
        execution_role = self.bootstrapper.get_resource("ServiceRole")
        task_definition = TaskDefinition(
            self.format_name("TaskDefinition"),
            "{}:{}".format(self.image_name, self.name.lower()),
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

    def create_build_files(self):
        self.create_index_html()
        self.create_docker_file()
        self.create_deploy_file()

    def create_deploy_file(self):
        with open(path.join(self.directory, "create_image.sh"), "w") as f:
            f.writelines(
                [
                    "#!/bin/bash\n",
                    "$(aws ecr get-login --no-include-email --registry-ids {})\n".format(
                        environ["AWS_ACCOUNT_ID"]
                    ),
                    "docker build . -t {}:{}\n".format(
                        self.image_name, self.name.lower()
                    ),
                    "docker push {}:{}\n".format(self.image_name, self.name.lower()),
                ]
            )

    def create_index_html(self):
        with open(path.join(self.directory, "index.html"), "w") as f:
            f.writelines(
                [
                    "<head><title>{}</title></head>\n".format(self.name),
                    "<body><h1>{}</h1></body>\n".format(self.name),
                ]
            )

    def create_docker_file(self):
        with open(path.join(self.directory, "Dockerfile"), "w") as f:
            f.writelines(["FROM nginx\n", "COPY ./index.html /usr/share/nginx/html\n"])
