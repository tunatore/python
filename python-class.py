class MyClass:
    list = []

    def __init__(self, data):
        self.list = data

    def count(self):
        return len(self.list)

    def append(self, data):
        self.list += data


m = MyClass([1, 2, 3, 4, 5])

print(m.count())

m.append([6, 7, 8, 9, 10, 12, 13, 14, 15, 16])

print(m.count())

for i in m.list:
    print(i, end=" ")
