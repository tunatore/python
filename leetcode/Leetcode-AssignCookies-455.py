class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort(reverse=True)
        s.sort(reverse=True)

        content_child = 0

        i = 0
        j = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                content_child += 1
                i += 1
                j += 1
            else:
                i += 1
        return content_child


s = Solution()
print(s.findContentChildren([1, 2, 3], [1, 1]))
print(s.findContentChildren([1, 2], [1, 2, 3]))
