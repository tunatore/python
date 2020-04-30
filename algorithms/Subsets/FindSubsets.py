# subsets


# Time complexity O(2**N) - exponential and Space complexity O(2**N) - exponential
def find_subsets(nums):
    subsets = []
    subsets.append([])
    for num in nums:
        i = 0
        n = len(subsets)
        while i < n:
            subset = list(subsets[i])
            subset.append(num)
            subsets.append(subset)
            i += 1
    return subsets


def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
