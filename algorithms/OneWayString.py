# Implement your function below.
def is_one_away(s1, s2):

    if len(s1) - len(s2) > 1 or len(s2) - len(s1) > 1:
        return False
    elif len(s1) == len(s2):
        different_element_count = 0
        for index,value in enumerate(s1):
            if s1[index] != s2[index]:
                different_element_count += 1
        if different_element_count > 1:
            return False
        else:
            return True
    else:
        different_element_count = 0
        s1_index = 0
        s2_index = 0
        while s1_index < len(s1) and s2_index < len(s2):
            if s1[s1_index] == s2[s2_index]:
                s1_index += 1
                s2_index += 1
            elif s1[s1_index] != s2[s2_index] and len(s1) > len(s2):
                s1_index += 1
                different_element_count += 1
            elif s1[s1_index] != s2[s2_index] and len(s2) > len(s1):
                s2_index += 1
                different_element_count += 1
        if different_element_count > 1:
            return False
        else:
            return True


# NOTE: The following input values will be used for testing your solution.
print(is_one_away("abcde", "abcd"))  # should return True
print(is_one_away("abde", "abcde"))  # should return True
print(is_one_away("a", "a"))  # should return True
print(is_one_away("abcdef", "abqdef"))  # should return True
print(is_one_away("abcdef", "abccef"))  # should return True
print(is_one_away("abcdef", "abcde"))  # should return True
print(is_one_away("aaa", "abc"))  # should return False
print(is_one_away("abcde", "abc"))  # should return False
print(is_one_away("abc", "abcde"))  # should return False
print(is_one_away("abc", "bcc"))  # should return False
