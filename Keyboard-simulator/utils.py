import json

def readFromJson():
    with open("statistics.json", 'r') as file:
        data = json.load(file)
        return data

def writeToJson(data):
    with open('statistics.json', 'w') as file:
        json.dump(data, file)
