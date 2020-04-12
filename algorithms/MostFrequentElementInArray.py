# Implement your function below.
def most_frequent(given_list):
    max_item = None
    max_count = -1

    d = dict([])
    for i in given_list:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1
        if d[i] > max_count:
            max_count = d[i]
            max_item = i
    return max_item


# NOTE: The following input values will be used for testing your solution.
# most_frequent(list1) should return 1
list1 = [1, 3, 1, 3, 2, 1]
print(most_frequent(list1))
# most_frequent(list2) should return 3
list2 = [3, 3, 1, 3, 2, 1]
print(most_frequent(list2))
# most_frequent(list3) should return None
list3 = []
print(most_frequent(list3))
# most_frequent(list4) should return 0
list4 = [0]
print(most_frequent(list4))
# most_frequent(list5) should return -1
list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]
print(most_frequent(list5))