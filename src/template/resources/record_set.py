from .resource import Resource


class RecordSet(Resource):
    type = "AWS::Route53::RecordSet"

    def __init__(self, name, record_set_name, hosted_zone_id, ip):
        super(RecordSet, self).__init__(RecordSet.type, name)
        self.properties = {
            "Name": record_set_name,
            "HostedZoneId": hosted_zone_id,
            "ResourceRecords": [ip],
            "Type": "A",
            "TTL": 300,
            "SetIdentifier": self.name,
            "Region": "us-west-2",  # gross
        }
