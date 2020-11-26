import yaml  # Install 'pyyaml' library.
import json

with open("data.yml") as f:
    data = yaml.load(f)
    print(data)
    print(json.dumps(data))
