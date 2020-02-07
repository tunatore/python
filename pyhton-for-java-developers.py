message = "test"
message1 = 'test2'

print("message: ", message)
print("message1: ", message1)
print("test3");
print("test4");
print("test5", end='');
print("test6")  # no new line

value = 0

if 0 == value:
    print("value is zero")
else:
    print("value is not zero")

number = 1
string = ''
stringMultipleLines = '''multiple lines
multiple lines2'''
multiple1, multiple2 = True, False

print("stringMultipleLines: ", stringMultipleLines)
print("multiple1: ", multiple1)
print("multiple2: ", multiple2)

# string methods

print(stringMultipleLines.find('lines'))  # charAt()
print(stringMultipleLines.index("ul"))  # indexOf()
print(len(stringMultipleLines))  # length()

strForReplace = "replace all these words"
print(strForReplace.replace("replace", ""))  # replace()

print(str(number) + string)  # str()

strForTrim = "     test       "
print(strForTrim.lstrip().rstrip(), end='');
print("addition")  # trim()

boolean = None
boolean1 = False
boolean2 = 0
emptyList = []
emptyCollection = ()

# List
# Unlike Java it can contain different types

list1 = []
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 100, 200]
A = [1, 2, 3, 'tuna']
B = [1, 2, 3, "python", "tuna"]



