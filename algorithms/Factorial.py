def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print("factorial:", 5, "is", factorial(5))
print("factorial:", 4, "is", factorial(4))
print("factorial:", 6, "is", factorial(6))