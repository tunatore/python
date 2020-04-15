class Dequeue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


dq = Dequeue()
print("dq size:", dq.size())

dq.add_front(0)
dq.add_rear(1)
dq.add_rear(2)

print("dq size:", dq.size())
print("front:", dq.remove_front())
print("rear:", dq.remove_rear())
print("is_empty:", dq.is_empty())

dq.add_rear(3)
dq.add_rear(4)
dq.add_rear(5)

print("front:", dq.remove_front())
print("front:", dq.remove_front())
print("front:", dq.remove_front())
print("front:", dq.remove_front())