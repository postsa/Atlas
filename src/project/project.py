from .service import Service
from src.project.bootstrapper import Bootstrapper


class Project(object):
    def __init__(self, name, *bootstrapper_dir_components):
        self.name = name
        self.bootstrapper = Bootstrapper(self.name, *bootstrapper_dir_components)
        self.services = []

    def bootstrap(self):
        self.bootstrapper.create()

    def add_service(self, service_name, *dir_components):
        service = Service(service_name, *dir_components)
        service.create()
        self.services.append(service)
