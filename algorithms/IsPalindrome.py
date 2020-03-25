import re # regular expressions


def isPalindrome1(self, s):
    """
    :type s: str
    :rtype: bool
    """
    if s is None:
        return True

    s = s.lower()
    str_replaced = re.sub('[^0-9a-z]+', '', s)
    return str_replaced == str_replaced[::-1]


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
print(isPalindrome1("A man, a plan, a canal: Panama"))
