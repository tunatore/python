# interpolation search formula
# //interpolation formula
# //probe = lowEnd + (((highEnd - lowEnd) * (item - data[lowEnd])) / (data[highEnd] - data[lowEnd]))
import math


def interpolation_search(arr, item):
    low_end = 0
    high_end = len(arr) - 1

    while low_end <= high_end and item >= arr[low_end] and item <= arr[high_end]:

        probe = math.floor(low_end + (((high_end - low_end) * (item - arr[low_end])) / (arr[high_end] - arr[low_end])))

        if arr[probe] == item:
            return probe

        if item > arr[probe]:
            low_end = probe + 1
        else:
            high_end = probe - 1
    return -1


array = [10, 40, 50, 90, 80, 70, 20, 30, 5, 4, 3, 2, 1, 0, 11, 12, 13, 14, 15, 16, 17, 18]
print("Sorted array: ", sorted(array))

print("found 6:", interpolation_search(sorted(array), 6) > -1)
print("found 2:", interpolation_search(sorted(array), 2) > -1)
print("found 700:", interpolation_search(sorted(array), 700) > -1)
print("found 600:", interpolation_search(sorted(array), 700) > -1)

