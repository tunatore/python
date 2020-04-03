from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        from queue import PriorityQueue
        priority_queue = PriorityQueue()

        for num in nums:
            priority_queue.put(-num)

        i = 1
        while not priority_queue.empty():
            if i == k:
                return -priority_queue.get()
            priority_queue.get()
            i += 1


s = Solution()
print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
