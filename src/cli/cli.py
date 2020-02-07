import argparse


class Cli(object):
    def __init__(self, atlas):
        self.atlas = atlas
        self.parser = argparse.ArgumentParser(description="Atlas project generation")
        self.parser.add_argument("new-project")
        self.parser.add_argument("list-projects")
        self.parser.add_argument("bootstrap")
        self.parser.add_argument("new-service")

    def new_project(self):
        self.atlas.create_project()

    def new_service(self):
        pass
