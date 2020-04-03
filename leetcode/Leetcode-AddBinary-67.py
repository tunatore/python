class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0:
                sum += int(a[i])
                i -= 1
            if j >= 0:
                sum += int(b[j])
                j -= 1
            result.append(str(sum % 2))
            carry = sum // 2

        if carry != 0:
            result.append(str(carry))

        return ''.join(reversed(result))


s = Solution()
print(s.addBinary("11", "1"))
print(s.addBinary("1010", "1011"))
