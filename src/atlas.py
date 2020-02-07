from src.db.db_factory import DbFactory
from src.project.project import Project


class Atlas(object):
    def __init__(self, db):
        self.db = db
        if self.db.persisted():
            self.copy(self.load())
        else:
            self.projects = {}

    def create_project(
        self, project_name, hosted_zone_id, dns_name, *bootstrapper_dir_components
    ):
        self.projects[project_name] = Project(
            project_name, hosted_zone_id, dns_name, *bootstrapper_dir_components
        )
        self.save()

    def bootstrap(self, project_name):
        project = self.projects[project_name]
        project.bootstrap()
        self.save()

    def add_service(self, project_name, service_name, *dir_components):
        project = self.projects[project_name]
        project.add_service(service_name, *dir_components)
        self.save()

    def save(self):
        self.db.save(self)

    def load(self):
        return self.db.load()

    def copy(self, atlas):
        self.projects = atlas.projects
