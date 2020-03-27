def rearrange(list):
    if list is None or len(list) == 0:
        return list
    return sorted([item for item in list if item < 0] + [item for item in list if item >= 0])


print(rearrange([1, -1, -2, -10, 4, -5, -3, -7, -6, -1, 1, 2, 7]))
