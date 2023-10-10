import json
file = "test_original.json"


def write_json(info, filename):
    with open(filename, "w") as f:
        json.dump(info, f, indent=4)


with open(file) as json_file:
    data = json.load(json_file)
    temp = data
    x = {"firstname": "John", "age": "50"}
    temp.append(x)
write_json(data, file)
