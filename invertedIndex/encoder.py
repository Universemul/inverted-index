
import json


class DefaultEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        if hasattr(obj, "to_json"):
            return obj.to_json()
        return json.JSONEncoder.default(self, obj)
