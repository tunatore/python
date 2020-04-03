class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if s is None or t is None:
            return False

        if len(s) != len(t):
            return False

        for c in set(s):
            if s.count(c) != t.count(c):
                return False
        return True


s = Solution()
str1 = "anagram"
str2 = "nagaram"

print(s.isAnagram(str1, str2))
