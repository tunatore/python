def fibonacci(x):
    if x <= 1:
        return x

    return fibonacci(x - 1) + fibonacci(x - 2)


for i in range(11):
    print(fibonacci(i), end = " ")
