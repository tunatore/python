class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if x < 0:
            negative = True
            x *= -1

        reverse = 0
        while x > 0:
            last_digit = x % 10
            x = x // 10
            reverse = (reverse * 10) + last_digit

        if reverse > 2 ** 31 - 1:
            return 0

        if negative:
            reverse *= -1
        return reverse


s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))