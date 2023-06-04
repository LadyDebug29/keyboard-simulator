import json


def readFromJson(path):
    with open(path, 'r') as file:
        return json.load(file)


def writeToJson(path, data):
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)