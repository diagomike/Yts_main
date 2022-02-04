import json

def loadJson(filename:str):
    with open(filename+'.json') as json_file:
        data = json.load(json_file)
        return data

def saveJson(filename:str,data:dict):
    with open(filename+".json", "w", encoding='utf8') as outfile:
        json.dump(data, outfile)
    print("Saved "+filename+".json")