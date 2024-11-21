import json


class ConfigReader:

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_json_data()

    def load_json_data(self):
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def get_url(self):
        return self.data.get("URL", None)

    def get_chrome_options(self):
        return self.data.get("Chrome_options", [])

    def get_chrome_option_by_index(self, index):
        options = self.get_chrome_options()
        if 0 <= index < len(options):
            return options[index]
        else:
            return None

    def get_data(self, set_key):
        subset = self.data.get(set_key, {})
        return subset.get("game"), subset.get("count")


