# Implement your function below.
def non_repeating(given_string):

    d = dict([])
    for i in given_string:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1

    for i in d.keys():
        if d[i] == 1:
            return i
    return None

# NOTE: The following input values will be used for testing your solution.
print(non_repeating("abcab")) # should return 'c'
print(non_repeating("abab")) # should return None
print(non_repeating("aabbbc")) # should return 'c'
print(non_repeating("aabbdbc")) # should return 'd'