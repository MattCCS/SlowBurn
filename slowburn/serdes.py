
import json


def serialize(value):
    return json.dumps(value)


def deserialize(value):
    return json.loads(value)
