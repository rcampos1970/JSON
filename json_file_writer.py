import json

file = "test_original.json"
data = [12, 45, "hello", "how u doin"]


def create_file_json(info, filename):
    with open(filename, "w") as f:
        json.dump(info, f)


create_file_json(data, file)
