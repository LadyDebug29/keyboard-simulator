import json


def readFromJson():
    with open("statistics.json", 'r') as file:
        content = file.read()
        data = json.loads(content)
        return data


def writeToJson(data):
    with open('statistics.json', 'w') as file:
        update_data = json.dumps(data)
        file.write(update_data)
