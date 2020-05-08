from operator import xor

message = "test"
message1 = 'test2'

print("message: ", message)
print("message1: ", message1)
print("test3")
print("test4")
print("test5", end='')
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
print(strForTrim.lstrip().rstrip(), end='')
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
print("C[4]: ", C[4])  # list.size()
print("len(C)", len(C))

D = C[:]  # every element in C list.clone()
print("D:", D)

# tuple
# immutable

tupleA = ()
tupleB = (1, 2, 3, 4, 5, 6)
tupleC = (2, 4, 'A')
tupleD = (1, 2, tupleB, tupleC)

print("tupleD: ", tupleD)
print("tupleD[2]", tupleD[2])

# dictionary
# key - value pairs

people = {'john': 123, "tom": 123}

print("john in people: ", 'john' in people)
people['john'] = 321
print(people['john'])
print(people.keys())

my_dict = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6'}
print("my_dict: ", my_dict)
print("len(my_dict): ", len(my_dict))
my_dict.pop(5)
print("my_dict: pop(5)", my_dict)
print("len(my_dict): ", len(my_dict))
my_dict.clear()
print("len(my_dict): ", len(my_dict))

print("xor 1 1:", xor(1, 1))
print("xor 1 0:", xor(1, 0))
print("xor 0 1:", xor(0, 1))
print("xor 0 0:", xor(0, 0))

# if
var1 = 100
if 100 == var1:
    print("var1 == 100")

# if else
var1 = 250
if 200 == var1:
    print("var1 == 200")
else:
    print("var1 != 200")

# if elif else
var1 = 250
if 200 == var1:
    print("var1 == 200")
elif 250 == var1:
    print("var1 == 250")
else:
    print("else value")

# multiple conditions
test1 = True
test2 = False

if test1 is False and test2 is True:
    print("Both conditions is True")

test1 = "test1"
test2 = "test2"

if test1 == "test1" and test2 == "test2":
    print("Both conditions == True")

# for loop
for i in range(0, 5):
    print("loop:", i)

# increased by 2
for j in range(0, 20, 2):
    print("loop: " + str(j))

# decreased by 1
for i in range(10, 0, -1):
    print("loop: " + str(i))

# for with break
for i in range(10, 0, -1):
    if i == 5:
        break
    print("loop: " + str(i))

# while
var = 1
while var < 10:
    var = var * 2
    print("var: ", var)

# iterate a list
values = ['1', '2', '3']
for value in values:
    print("value", value)

# iterate a tuple
values = ('1', '2', '3')
for value in values:
    print("value (tuple)", value)

# list as stack
stack = [1]
stack.append(2)
print("list as stack:", stack.pop())  # pop 2

# set
set1 = {1, 1, 2, 2, 3, 3, 4, 5}
print(set1)

set2 = set([1, 1, 2, 2, 3, 3, 4, 5])
print(set2)

# for loop with index
list1 = [1, 2, 3, 4, 5]
for i in range(1, len(list1) + 1):
    print(list1[i - 1], end="")

print()

# for loop with index reverse
for i in range(len(list1) - 1, -1, -1):
    print(list1[i], end="")

print()
test = [[0 for x in range(10)]]
print(test)

# python counter
import collections

c = collections.Counter(["a", "a", "a", "a", "a", "b", "c"])
print(c)
c.update("aaaaaaaaaabbbbccc")
print(c)

for char in "abc":
    print((char, c[char]))

# counter elements
print(list(c.elements()))

# counter most common
for char, count in c.most_common(2):
    print("%s: %d" % (char, count))

print(c.items())
print(c.keys())
print(c.values())

# all method
list = [2, 2, 2, 2, 2]
print(all([val == 2 for val in list]))

dict = {}
dict["a"] = 0
dict["b"] = 0
dict["c"] = 0
print(dict)
print(all([val == 0 for val in dict.values()]))

from itertools import chain

list = [[10, 20, 30], [1, 2, 3], [0, 1], [100, 200, 300]]
print(sorted(chain(*list)))
