def check_permutation(str1, str2):

    if str1 is None or str2 is None:
        return False

    if len(str1) != len(str2):
        return False

    str1_sorted = sorted(str1.lower())
    str2_sorted = sorted(str2.lower())

    return str1_sorted == str2_sorted


print(check_permutation("test", "tset"))
print(check_permutation("test", "tse"))
print(check_permutation("test", "tsett"))
print(check_permutation("abc", "bca"))


