from unittest import TestCase
from src.template.resources import Vpc


class VpcTest(TestCase):
    def setUp(self):
        self.vpc = Vpc("test", "0.0.0.0/16")

    def test_has_correct_values(self):
        self.assertEqual("test", self.vpc.name)
        self.assertEqual("AWS::EC2::VPC", self.vpc.type)
        self.assertDictEqual({"CidrBlock": "0.0.0.0/16"}, self.vpc.properties)
