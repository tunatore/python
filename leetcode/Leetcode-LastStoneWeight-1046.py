# Python 3 solution
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if len(stones) < 2:
            return stones[0]

        from queue import PriorityQueue
        priority_queue = PriorityQueue()

        for num in stones:
            priority_queue.put(-num)

        while not priority_queue.empty() and priority_queue.qsize() > 1:
            stone1 = priority_queue.get()
            stone2 = priority_queue.get()
            priority_queue.put(stone1 - stone2)

        if priority_queue.empty():
            return 0
        else:
            return abs(priority_queue.get())


s = Solution()
print(s.lastStoneWeight([1, 3]))
print(s.lastStoneWeight([2, 7, 4, 1, 8, 1]))
print(s.lastStoneWeight([4, 3, 4, 3, 2]))
