class Stack:

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


s = Stack()

print(s.pop())

s.push(1)
s.push(2)

print(s.pop())
print(s.pop())
print(s.pop())

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)

print(s.peek())

s.push(8)

print(s.peek())