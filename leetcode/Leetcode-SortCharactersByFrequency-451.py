# Python3 solution


class Solution:
    def frequencySort(self, s: str) -> str:
        if s is None or len(s) == 0:
            return s

        char_dict = {}
        for c in s:
            if c in char_dict:
                char_dict[c] += 1
            else:
                char_dict[c] = 1

        from queue import PriorityQueue
        priority_queue = PriorityQueue()

        for c in char_dict:
            priority_queue.put((-char_dict[c], c))

        result = ""
        while not priority_queue.empty():
            char_tuple = priority_queue.get()
            for count in range(-char_tuple[0]):
                result += char_tuple[1]

        return result


s = Solution()
print(s.frequencySort("tree"))
print(s.frequencySort("cccaaa"))
print(s.frequencySort("Aabb"))