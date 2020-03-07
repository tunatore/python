def decimal_to_binary_number(decimal_number):
    remainder_stack = []

    while decimal_number > 0:
        remainder = decimal_number % 2
        remainder_stack.append(remainder)
        decimal_number = decimal_number // 2

    binary_string = ""
    while not len(remainder_stack) == 0:
        binary_string += str(remainder_stack.pop())
    return binary_string


def binary_to_decimal(binary_number):
    number = 0
    for i in range(0, len(binary_number)):
        number += int(binary_number[i]) * (2 ** (len(binary_number) - 1 - i))
    return number


print("1:", decimal_to_binary_number(1))
print("2:", decimal_to_binary_number(2))
print("5:", decimal_to_binary_number(5))
print("6:", decimal_to_binary_number(6))
print("8:", decimal_to_binary_number(8))
print("10:", decimal_to_binary_number(10))
print("1500:", decimal_to_binary_number(1500))

print("1:", binary_to_decimal("1"))
print("10:", binary_to_decimal("10"))
print("101:", binary_to_decimal("101"))
print("110:", binary_to_decimal("110"))
print("1000:", binary_to_decimal("1000"))
print("1010:", binary_to_decimal("1010"))
print("10111011100:", binary_to_decimal("10111011100"))