class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        char_array = list(str(x))

        for i in range(0, len(char_array) / 2):
            if char_array[i] == char_array[len(char_array) - (i + 1)]:
                continue
            else:
                return False
        return True

        