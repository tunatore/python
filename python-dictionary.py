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