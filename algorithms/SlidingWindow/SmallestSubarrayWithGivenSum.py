# sliding window
import math


# Time complexity O(N) and Space complexity O(1)
def smallest_subarray_with_given_sum(s, arr):

    window_sum = 0
    window_start_index, window_end_index = 0, 0
    min_length = math.inf
    min_length_sum = 0

    for window_end_index in range(len(arr)):
        window_sum += arr[window_end_index]
        min_length_sum += 1
        while window_sum >= s:
            if min_length_sum < min_length:
                min_length = min_length_sum
            window_sum -= arr[window_start_index]
            min_length_sum -= 1
            window_start_index += 1

    if min_length == math.inf:
        return 0

    return min_length


def main():
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6, 5])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(6, [2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(18, [2])))

main()