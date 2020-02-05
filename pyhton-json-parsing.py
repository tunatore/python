# Created on Jul 30, 2013
# @author: tunatore

import json

# you can create a json structure
pythonStructure = {'JavaLevel': 'Expert', 'PythonLevel': "Beginner", 'C#Level': "Good"}

print("Python Structure = ", pythonStructure)

# dumps will load python structure as json
print("JSON Converted Structure = ", json.dumps(pythonStructure))
print("JSON Converted Structure Sorted Keys = ", json.dumps(pythonStructure, sort_keys=True))

# pretty printed JSON
print("pretty printed JSON \n")
print(json.dumps(pythonStructure, sort_keys=True, indent=5, separators=(',', ' : ')))

# dumps will load json structure as python structure
print("Python Structure = ", (json.loads(json.dumps(pythonStructure))))

# another python struct conversion

pythonData = dict(
    key1="Val 1",
    key2="Val 2",
    key3="Val 3",
    key4=4
)

print("JSON Converted Structure = ", json.dumps(pythonData, sort_keys=True))
# loading and parsing JSON data from url
import urllib.request

url = "http://carma.org/api/1.1/searchLocations?name=Idaho"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
loadJSON = json.loads(response.read().decode('utf-8'))
print(json.dumps(loadJSON, indent=4, sort_keys=True))

# get carbon JSON item
carbon = loadJSON[0]['carbon']
print("carbon future", carbon['future'])
print("carbon past", carbon['past'])
print("carbon present", carbon['present'])
