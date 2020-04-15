# intersection of two sorted arrays


def intersection_of_arrays(A, B):
    i = 0
    j = 0

    intersection_result = []

    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i - 1]:
                intersection_result.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return intersection_result


A = [3, 3, 4, 5, 6, 7, 8, 8, 9, 10]
B = [3, 5, 6, 15, 16, 17, 18]
print(intersection_of_arrays(A, B))
