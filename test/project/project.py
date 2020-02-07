from src.project.project import Project
from unittest import TestCase


class ProjectTest(TestCase):
    def setUp(self):
        self.project = Project("test", "zone" "test.com" "not", "a", "dir")

    def test_has_bootstrapper(self):
        self.assertIsNotNone(self.project.bootstrapper)
        self.assertEqual("test", self.project.bootstrapper.name)

    def test_can_add_service(self):
        self.project.add_service("service", "dir", "components")
        self.assertEqual(1, len(self.project.services))
        self.assertEqual("service", self.project.services[0].name)
