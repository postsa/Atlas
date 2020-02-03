from .project_component import ProjectComponent
from src.template.resources import *
from src.template.resource_resolvers import *


class Bootstrapper(ProjectComponent):
    def create_resources(self):
        vpc = Vpc("{}Vpc".format(self.name), "12.0.0.0/16").with_self_ref_output(
            "Id", "The id of the vpc"
        )
        self.template.add_resource(vpc)
        internet_gateway = InternetGateway(self.format_name("InternetGateway"))
        self.template.add_resource(internet_gateway)
        vpc_gateway_mapping = VpcGatewayAttachment(
            self.format_name("VpcGatewayMapping"),
            internet_gateway.get_name_resolver(),
            vpc.get_name_resolver(),
        )
        self.template.add_resource(vpc_gateway_mapping)
        public_subnet = Subnet(
            self.format_name("PublicSubnet"),
            "12.0.1.0/24",
            vpc.get_name_resolver(),
            True,
        ).with_self_ref_output("Id", "The id of the public subnet")
        self.template.add_resource(public_subnet)
        private_subnet = Subnet(
            self.format_name("PrivateSubnet"),
            "12.0.2.0/24",
            vpc.get_name_resolver(),
            False,
        ).with_self_ref_output("Id", "The id of the private subnet")
        self.template.add_resource(private_subnet)
        elastic_ip = ElasticIp(
            self.format_name("ElasticIp"), "vpc"
        ).with_self_ref_output("Address", "Elastic ip address")
        self.template.add_resource(elastic_ip)
        nat_gateway = NatGateway(
            self.format_name("NatGateway"),
            GetAttResolver(elastic_ip.name, "AllocationId"),
            public_subnet.get_name_resolver(),
        )
        self.template.add_resource(nat_gateway)
        private_route_table = RouteTable(
            self.format_name("PrivateRouteTable"), vpc.get_name_resolver()
        )
        self.template.add_resource(private_route_table)
        private_internet_route = Route(
            "PrivateInternetRoute",
            nat_gateway.get_name_resolver(),
            private_route_table.get_name_resolver(),
            "0.0.0.0/0",
        )
        self.template.add_resource(private_internet_route)
        private_route_table_subnet_association = SubnetRouteTableAssociation(
            "PrivateRouteTableSubnetAssociation",
            private_route_table.get_name_resolver(),
            private_subnet.get_name_resolver(),
        )
        self.template.add_resource(private_route_table_subnet_association)
        public_route_table = RouteTable(
            self.format_name("PublicRouteTable"), vpc.get_name_resolver()
        )
        self.template.add_resource(public_route_table)
        public_internet_route = Route(
            "PublicInternetRoute",
            nat_gateway.get_name_resolver(),
            public_route_table.get_name_resolver(),
            "0.0.0.0/0",
        )
        self.template.add_resource(public_internet_route)
        public_route_table_subnet_association = SubnetRouteTableAssociation(
            "PublicRouteTableSubnetAssociation",
            public_route_table.get_name_resolver(),
            public_subnet.get_name_resolver(),
        )
        self.template.add_resource(public_route_table_subnet_association)
        security_group = SecurityGroup(
            self.format_name("SecurityGroup"),
            vpc.get_name_resolver(),
            "Internet egress and ssh ingress",
            "{} Security Group".format(self.name),
        ).with_self_ref_output("ResourceId", "Security group resource id")
        self.template.add_resource(security_group)
        allow_all_egress = SecurityGroupEgress(
            "AllowAllEgress",
            "0.0.0.0/0",
            GetAttResolver(security_group.name, "GroupId"),
            "-1",
        )
        self.template.add_resource(allow_all_egress)
        allow_ssh_ingress = SecurityGroupIngress(
            "AllowSshIngress",
            "0.0.0.0/0",
            GetAttResolver(security_group.name, "GroupId"),
            "tcp",
            "22",
            "22",
        )
        self.template.add_resource(allow_ssh_ingress)
