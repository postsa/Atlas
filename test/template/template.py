from unittest import TestCase

from src.template.resource_resolvers.get_att_resolver import GetAttResolver
from src.template.template import Template
from src.template.resources.vpc import Vpc


class TemplateTest(TestCase):
    def setUp(self):
        self.template = Template()

    def test_add_resource(self):
        self.template.add_resource(Vpc("test", "10.0.0.0/16"))
        self.assertEqual(1, len(self.template.resources))
        vpc = self.template.resources["test"]
        self.assertEqual("test", vpc.name)

    def test_serialize(self):
        self.template.add_resource(Vpc("Test", "10.0.0.0/16"))
        print(self.template.template())

    def test_serialize_object_with_attr_output(self):
        self.template.add_resource(
            Vpc("Test", "10.0.0.0/16")
            .with_attr_output("Cidr", GetAttResolver("Test", "Cidr"))
            .with_self_ref_output("Id")
        )
        print(self.template.template())
