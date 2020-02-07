from src.project.project_component import ProjectComponent


class ServiceComponent(ProjectComponent):
    def __init__(
        self, name, project_name, hosted_zone_id, dns_name, bootstrapper, *path_dirs
    ):
        self.bootstrapper = bootstrapper
        super(ServiceComponent, self).__init__(
            name, project_name, hosted_zone_id, dns_name, *path_dirs
        )

    def format_name(self, resource):
        return "{}{}{}".format(self.project_name, self.name, resource)
