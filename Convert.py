import json
import yaml

with open('data.json', 'r') as file:
    data = json.load(file)

yaml_data = yaml.dump(data, allow_unicode=True)

print(yaml_data)