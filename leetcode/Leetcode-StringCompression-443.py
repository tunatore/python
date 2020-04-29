class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        last_index = 0
        slow_index = 0
        while slow_index < len(chars):
            current_index = slow_index
            chars[last_index] = chars[slow_index]
            while current_index < len(chars) \
                    and chars[slow_index] == chars[current_index]:
                current_index += 1

            last_index += 1
            if current_index - slow_index > 1:
                count = str(current_index - slow_index)
                for c in count:
                    chars[last_index] = c
                    last_index += 1
            slow_index = current_index

        return last_index


s = Solution()
print(s.compress(["a", "a", "b", "b", "c", "c", "c"]))
print(s.compress(["a"]))
print(s.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
print(s.compress(["a","a","a","b","b","a","a"]))
