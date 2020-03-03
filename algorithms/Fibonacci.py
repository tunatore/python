def fibonacci(x, memo={}):
    if x <= 1:
        return x

    if x not in memo:
        memo[x] = fibonacci(x - 1) + fibonacci(x - 2)

    return memo[x]


for i in range(11):
    print(fibonacci(i), end=" ")
