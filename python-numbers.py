print((8).bit_length())

# float division
print(10 / 2)

# quotient and remainder
print(divmod(40, 2))
print(divmod(11, 2))
print(divmod(5, 2))

# round
print(round(100.70, -2))
print(round(100.767, 2))

# binary
print(bin(8))
print(bin(100))

# hexadecimal
print(hex(100))

# random
import random

values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))
print(random.sample(values, 2))
random.shuffle(values)
print(values)

# create random integers
print(random.randint(0, 10))

# power
print(pow(2,6))
