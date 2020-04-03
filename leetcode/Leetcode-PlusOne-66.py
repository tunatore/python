class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits is None:
            return 1

        result = []
        i = len(digits) - 1

        carry = 1
        while i >= 0:
            sum = carry
            sum += digits[i]
            result.append(str(sum % 10))
            carry = sum // 10
            i -= 1

        if carry != 0:
            result.append(str(carry))

        return ''.join(reversed(result))


s = Solution()
print(s.plusOne([1, 2, 3]))
print(s.plusOne([4, 3, 2, 1]))
