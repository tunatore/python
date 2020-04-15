def sorted_merge_arrays(arr1, arr2):

    index_arr1 = len(arr1) - len(arr2) - 1
    index_arr2 = len(arr2) - 1

    while index_arr1 >= 0 and index_arr2 >= 0:
        if arr1[index_arr1] > arr2[index_arr2]:
            arr1[index_arr1 + index_arr2 + 1] = arr1[index_arr1]
            index_arr1 -= 1
        else:
            arr1[index_arr1 + index_arr2 + 1] = arr2[index_arr2]
            index_arr2 -= 1
    while index_arr2 >= 0:
        arr1[index_arr2] = arr2[index_arr2]
        index_arr2 -= 1
    return arr1


arr1 = [10, 11, 12, 13, 14, 15, 16, None, None, None, None]
arr2 = [6, 7, 20, 25]
print(sorted_merge_arrays(arr1, arr2))
