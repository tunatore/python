my_dict = {}
my_dict[1] = 1
my_dict[2] = 2
my_dict[3] = 3
my_dict[4] = 4
my_dict[5] = 5

key = 2
print(key in my_dict)

del my_dict[2]
print(my_dict)

my_dict_str = {'tuna': 'test', 'tuna1': 'test2'}
print(my_dict_str)

print("keys", my_dict_str.keys())
print("values", my_dict_str.values())
print("items", my_dict_str.items())
print("get(key)", my_dict_str.get('tuna'))
print("get(key,alt)", my_dict_str.get('key', 'otherwise'))

# iterate a dictionary
values = {'value': '123456', 'value1': '123456'}
for key in values:
    print("value (dictionary)", values[key])

for key, value in values.items():
    print("key", key, "value (dictionary)", value)

for key in values.keys():
    print("key", key)

for value in values.values():
    print("value", value)

for key in sorted(values.keys()):
    print("key", key)

for key in reversed(values.keys()):
    print("key", key)

import collections

# keep the insertion order in Dictionary
orderedDictionary = collections.OrderedDict()
orderedDictionary[0] = 0
orderedDictionary[1] = 1
orderedDictionary[2] = 2
orderedDictionary[3] = 3
orderedDictionary[4] = 4
orderedDictionary[5] = 5
for i in orderedDictionary.keys():
    print(i, end="->")

