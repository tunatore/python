str = "Text"

print("->", str.center(100), "<-")

str = "11223344556622222"
# returns the number of occurrences
print(str.count("2"))

# index of the first occurrence
print("index:", str.find("2"))

# string to number

s = '10'
print(int(s))

# char array

str1 = "chararray"
print(list(str1))

# slicing
# seq [start:end:step]

str = "Test string"
print(str[-1])
print(str[-2])
print(str[-2:])
print(str[0::2])
print(str[0:-2])

name = "Text"
print(name.rjust(50,"-"))
print(name.ljust(50,"-"))

# format
print("{0} {1}".format("1", "2"))
print("{} {}".format("1", "2"))

text_with_lines = "text1\ntext2\ntext3"
print(text_with_lines.splitlines())

#split
print(text_with_lines.split("\n"))

#strip
print("text1|text2".strip("text1"))

#swapcase
print("text".swapcase())
print("text".capitalize())
print("text".upper())
print("TEXT".lower())

# index or find
# index throw exception

print("text1".find("t"))
print("text1".find("a"))
print("text1".rfind("t"))
print("text1".rfind("1"))

# count(t,start,end)
print("text1".count("t", 0, -1))

# replace (t,u,n) - replace n times
print("text1".replace("t", "r", 1))
print("text1".replace("t", "r", 2))

