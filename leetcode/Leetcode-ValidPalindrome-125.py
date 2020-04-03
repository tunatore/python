import re  # regular expressions


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return True

        s = s.lower()
        str_replaced = re.sub('[^0-9a-z]+', '', s)
        return str_replaced == str_replaced[::-1]


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
