from src.project import Project


class Atlas(object):
    def __init__(self):
        self.projects = {}

    def create_project(self, project_name, *bootstrapper_dir_components):
        self.projects[project_name] = Project(
            project_name, *bootstrapper_dir_components
        )

    def bootstrap(self, project_name):
        project = self.projects[project_name]
        project.bootstrap()

    def add_service(self, service_name, service_dir):
        pass
