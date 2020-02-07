from .service import Service
from src.project.bootstrapper import Bootstrapper


class Project(object):
    def __init__(self, name, hosted_zone_id, dns_name, *bootstrapper_dir_components):
        self.name = name
        self.hosted_zone_id = hosted_zone_id
        self.dns_name = dns_name
        self.bootstrapper = Bootstrapper(
            self.name, self.name, hosted_zone_id, dns_name, *bootstrapper_dir_components
        )
        self.services = []

    def bootstrap(self):
        self.bootstrapper.create()

    def add_service(self, service_name, *dir_components):
        service = Service(
            service_name,
            self.name,
            self.hosted_zone_id,
            self.dns_name,
            self.bootstrapper,
            *dir_components,
        )
        service.create()
        self.services.append(service)
