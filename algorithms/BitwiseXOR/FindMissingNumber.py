# xor of same number = 0
# 1 ^ 1 = 0
# 29 ^ 29 = 0

# xor of a number with 0 is the same number
# 1 ^ 0 = 1
# 29 ^ 0 = 29


def find_missing_number(arr):
    if arr is None:
        return None

    # xor of all numbers from 1 to N
    xor1 = 1
    for i in range(2, len(arr) + 2):
        xor1 = xor1 ^ i

    # xor of all numbers in arr
    xor2 = arr[0]
    for i in range(1, len(arr)):
        xor2 = xor2 ^ arr[i]

    return xor1 ^ xor2


def main():
    arr = [1, 5, 2, 6, 4]
    print('Missing number is:' + str(find_missing_number(arr)))


main()
