def isPalindrome1(str):
    return str == str[::-1]


def isPalindrome2(str):
    for i in range(0, len(str) // 2):
        if not str[i] == str[len(str) - i - 1]:
            return False
    return True


print(isPalindrome1("yes"))
print(isPalindrome1("teet"))
print(isPalindrome2("teet"))
print(isPalindrome2("yes"))
print(isPalindrome2("test"))
print(isPalindrome2(""))
print(isPalindrome2("123456"))
