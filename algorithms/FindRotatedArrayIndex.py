def find_rotated_index(A):

    start = 0
    end = len(A) - 1

    while start < end:
        mid = (start + end) // 2
        if A[mid] > A[end]:  # search second half of the array
            start = mid + 1
        elif A[mid] <= A[end]:  # search first half of the array
            end = mid
    return A[start]


A = [2, 3, 4, 5, 6, 7, 8, 1]
print(find_rotated_index(A))

A = [6, 7, 8, 0, 1, 2, 3]
print(find_rotated_index(A))
