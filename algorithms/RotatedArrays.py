# Implement your function below.
def is_rotation(list1, list2):
    if len(list1) != len(list2):
        return False

    item = list1[0]
    index_list1_item = None

    for index,value in enumerate(list2):
        if item == value:
            index_list1_item = index
            break

    if index_list1_item is None:
        return False

    # list 2
    for index, value in enumerate(list1):
        index_list2 = (index_list1_item + index) % len(list1)
        if list1[index] != list2[index_list2]:
            return False
    return True


# NOTE: The following input values will be used for testing your solution.
list1 = [1, 2, 3, 4, 5, 6, 7]
list2a = [4, 5, 6, 7, 8, 1, 2, 3]
# is_rotation(list1, list2a) should return False.
print(is_rotation(list1, list2a))
list2b = [4, 5, 6, 7, 1, 2, 3]
# is_rotation(list1, list2b) should return True.
print(is_rotation(list1, list2b))
list2c = [4, 5, 6, 9, 1, 2, 3]
# is_rotation(list1, list2c) should return False.
print(is_rotation(list1, list2c))
list2d = [4, 6, 5, 7, 1, 2, 3]
# is_rotation(list1, list2d) should return False.
print(is_rotation(list1, list2d))
list2e = [4, 5, 6, 7, 0, 2, 3]
# is_rotation(list1, list2e) should return False.
print(is_rotation(list1, list2e))
list2f = [1, 2, 3, 4, 5, 6, 7]
# is_rotation(list1, list2f) should return True.
print(is_rotation(list1, list2f))
list2g = [7, 1, 2, 3, 4, 5, 6]
# is_rotation(list1, list2g) should return True.
print(is_rotation(list1, list2g))