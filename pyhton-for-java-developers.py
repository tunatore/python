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

a = b = c = d = 1
e = 2

print("a b c d e: ", a, b, c, d, e)

var = 0
var = "a"

print("var: ", var)

# List
# Unlike Java it can contain different types

list1 = []
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 100, 200]
A = [1, 2, 3, 'tuna']
B = [1, 2, 3, "python", "tuna"]
C = [1, 2, 3, A, B]

print("C: ", C)

C.append("4")  # list.add()
C.append("5")  # list.add()
C.append("6")  # list.add()

print("C: ", C)

print("C[0]: ", C[0])  # list.get(i)
print("C[4]: ", C[4])   # list.size()
print("len(C)", len(C))

D = C[:]  # every element in C list.clone()
print("D:", D)

#tuple
#immutable

tupleA = ()
tupleB = (1, 2, 3, 4, 5, 6)
tupleC = (2, 4, 'A')
tupleD = (1, 2, tupleB, tupleC)

print("tupleD: ", tupleD)
print("tupleD[2]", tupleD[2])

#dictionary
# key - value pairs

people = {'john': 123, "tom": 123}

print("john in people: ", 'john' in people)
people['john'] = 321
print(people['john'])
print(people.keys())
