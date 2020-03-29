import json
import yaml
from hello.hello import Person
class Converter:
    def __init__(self, filename, out_file):
        self.filename = filename
        self.out_file = out_file
    def yaml_to_json(self, filename = None):
        if not filename:
            filename = self.filename
        with open(filename) as f:
            data = yaml.safe
            _load(f.read())
        with open (self.out_file, "w") as f:
            f.write(json.dumps(data))
    def json_to_yaml(self, filename = None):
        if not filename:
            filename = self.filename
        with open(filename) as f:
            data = json.loads(f.read())
        with open (self.out_file, "w") as f:
            yaml.dump(data,f)
c = Converter("coding.json","category.yaml")
#c.yaml_to_json()
c.json_to_yaml()

