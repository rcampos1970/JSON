import json

file = 'json-files/names.json'


def deconstruction_var_json():
    with open(file, 'r') as json_file:
        data = json.load(json_file)
        print(data)


deconstruction_var_json()
