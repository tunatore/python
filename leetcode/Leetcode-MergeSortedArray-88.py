class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        index = 0
        index2 = 0
        for _ in range(0, len(nums1)):
            for _ in range(0, len(nums2[:n])):
                if index2 > len(nums2) - 1:
                    break
                if nums1[index] >= nums2[index2]:
                    nums1.insert(index, nums2[index2])
                    index = index + 1
                    index2 = index2 + 1
                elif nums1[index] < nums2[index2]:
                    if index - index2 - m >= 0:
                        nums1[index] = nums2[index2]
                        index = index + 1
                        index2 = index2 + 1
            index = index + 1
        del nums1[m + n:]
        return nums1


s = Solution()

print(s.merge([0, 0, 0, 0, 0], 0, [1, 2, 3, 4, 5], 5))
print(s.merge([2, 0], 1, [1], 1))
print(s.merge([1, 0], 1, [2], 1))
print(s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(s.merge([1, 2, 3, 0, 0, 0], 3, [4, 5, 6], 3))
