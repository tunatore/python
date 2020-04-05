# Implement your function below.
def common_elements(list1, list2):
    list1_index = 0
    list2_index = 0
    result = []

    while list1_index < len(list1) and list2_index < len(list2):
        if list1[list1_index] == list2[list2_index]:
            result.append(list1[list1_index])
            list1_index += 1
            list2_index += 1
        elif list1[list1_index] > list2[list2_index]:
            list2_index += 1
        elif list1[list1_index] < list2[list2_index]:
            list1_index += 1
    return result


# NOTE: The following input values will be used for testing your solution.
list_a1 = [1, 3, 4, 6, 7, 9]
list_a2 = [1, 2, 4, 5, 9, 10]
# common_elements(list_a1, list_a2) should return [1, 4, 9] (a list).
print(common_elements(list_a1, list_a2))

list_b1 = [1, 2, 9, 10, 11, 12]
list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
# common_elements(list_b1, list_b2) should return [1, 2, 9, 10, 12] (a list).
print(common_elements(list_b1, list_b2))

list_c1 = [0, 1, 2, 3, 4, 5]
list_c2 = [6, 7, 8, 9, 10, 11]
# common_elements(list_b1, list_b2) should return [] (an empty list).
print(common_elements(list_c1, list_c2))