from .frontend import Frontend


class Service:
    def __init__(self, name, project_name, hosted_zone_id, bootstrapper, *path_dirs):
        self.name = name
        self.project_name = project_name
        self.hosted_zone_id = hosted_zone_id
        self.bootstrapper = bootstrapper
        self.frontend = Frontend(
            name, project_name, hosted_zone_id, bootstrapper, *path_dirs
        )

    def create(self):
        self.frontend.create()
