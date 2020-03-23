class Stack:
    def __init__(self):
        self.stack_list = []

    def isEmpty(self):
        return len(self.stack_list) == 0

    def top(self):
        if self.isEmpty():
            return None
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.isEmpty():
            return None
        return self.stack_list.pop()


def sort_stack(stack):

    temp_stack = Stack()

    while stack.size() != 0:
        stack_item = stack.pop()

        if temp_stack.size() == 0:
            temp_stack.push(stack_item)
        else:
            while temp_stack.size() != 0 and temp_stack.top() <= stack_item:
                stack.push(temp_stack.pop())
            temp_stack.push(stack_item)
    return temp_stack


stack = Stack()
stack.push(10)
stack.push(6)
stack.push(4)
stack.push(8)
stack.push(-1)
stack.push(25)
stack.push(75)

stack = sort_stack(stack)
# after sorting
print([stack.pop() for i in range(stack.size())])

