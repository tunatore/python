# sliding window


# Time complexity: O(N*M) and Space complexity: O(1)
def max_sub_array_of_size_k_brute_force(k, arr):
    max_sum = 0
    for i in range(len(arr) - k + 1):
        window_sum = 0.0
        for j in range(i, i + k):
            window_sum += arr[j]
        if window_sum > max_sum:
            max_sum = window_sum
    return max_sum


# windowStart and windowEnd define the boundaries
# Time complexity: O(N) and Space complexity: O(1)
def max_sub_array_of_size_k(k, arr):
    max_sum = -1
    window_sum, window_start = 0.0, 0
    for windowEnd in range(len(arr)):
        window_sum += arr[windowEnd]
        if windowEnd >= k - 1:
            if window_sum > max_sum:
                max_sum = window_sum
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum


print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))
print(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]))
print(max_sub_array_of_size_k_brute_force(3, [2, 1, 5, 1, 3, 2]))
