import json


def readFromJson():
    with open("utils/statistics.json", 'r') as file:
        content = file.read()
        data = json.loads(content)
        return data


def writeToJson(data):
    with open('utils/statistics.json', 'w') as file:
        update_data = json.dumps(data)
        file.write(update_data)
