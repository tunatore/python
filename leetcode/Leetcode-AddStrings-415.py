class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = []
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0:
                sum += ord(num1[i]) - ord('0')
                i -= 1
            if j >= 0:
                sum += ord(num2[j]) - ord('0')
                j -= 1
            result.append(str(sum % 10))
            carry = sum // 10

        if carry != 0:
            result.append(str(carry))

        return ''.join(reversed(result))


s = Solution()
print(s.addStrings("123", "456"))
print(s.addStrings("100", "200"))
print(s.addStrings("1000", "200"))
print(s.addStrings("100", "100"))
print(s.addStrings("17", "18"))
print(s.addStrings("1", "1"))
print(s.addStrings("1", "2"))