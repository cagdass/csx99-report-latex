import json

jsonFile = open('./contents.json', 'r')
jsonString = jsonFile.read()
jsonFile.close()

contents = json.loads(jsonString)

print contents['directories']['workDone']
