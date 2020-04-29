class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest_common_prefix = ""
        if strs is None or len(strs) == 0:
            return longest_common_prefix

        i = 0
        for c in strs[0]:
            for index in range(1, len(strs)):
                if i >= len(strs[index]) or c != strs[index][i]:
                    return longest_common_prefix
            longest_common_prefix += c
            i += 1
        return longest_common_prefix


s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))