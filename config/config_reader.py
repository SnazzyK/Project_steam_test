import json


FILE_CONFIG = "config/config.json"
class ConfigReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_json_data()

    def load_json_data(self):
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def get_data(self, key, num=None):
        value = self.data.get(key)
        if isinstance(value, dict):
            return list(value.values())
        elif isinstance(value, list):
            if num is not None:
                return value[num]
        elif isinstance(value, str):
            return value
