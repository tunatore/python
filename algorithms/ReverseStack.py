# reverse stack without using any additional structures


def reverse(stack):
    if stack is None:
        return None

    if len(stack) == 0:
        return stack

    temp = stack.pop()
    reverse(stack)
    insert_bottom(stack, temp)
    return stack


def insert_bottom(stack, val):
    if len(stack) == 0:
        stack.append(val)
        return

    temp = stack.pop()
    insert_bottom(stack, val)
    stack.append(temp)


stack = [1, 2, 3, 4, 5, 6]
print(reverse(stack))
