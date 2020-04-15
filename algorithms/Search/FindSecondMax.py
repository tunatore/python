# Time complexity O(N) and Space complexity O(1)
def findSecondMaximum(list):
    if list is None or len(list) < 2:
        return list

    max = second_max = float("-inf")

    for i in range(len(list)):
        if list[i] > max and list[i] > second_max:
            second_max = max
            max = list[i]
        elif list[i] > second_max and list[i] != max:
            second_max = list[i]
    return second_max


print(findSecondMaximum([1, 100, 80, 5, 6, 85, 91, 10, 86]))
