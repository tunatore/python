def isAnagram(s1, s2):
    s1 = set(s1.replace(" ", ""))
    s2 = set(s2.replace(" ", ""))
    return s1 == s2


def isAnagram2(s1, s2):

    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    d = dict([])

    for s in s1:
        if s not in d:
            d[s] = 1
        else:
            d[s] += 1
    for s in s2:
        if s not in d:
            d[s] = 1
        else:
            d[s] -= 1

    for s in d:
        if d[s] != 0:
            return False
    return True


print("isAnagram:", isAnagram("test", "test2"))
print("isAnagram:", isAnagram2("test", "test2"))