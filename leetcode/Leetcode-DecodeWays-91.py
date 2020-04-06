class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s is None or len(s) <= 1:
            return 0 if s[0] == '0' else 1

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(s) + 1):
            digit = int(s[i-1:i])
            two_digits = int(s[i-2:i])

            if digit >= 1:
                dp[i] += dp[i-1]
            if 10 <= two_digits <= 26:
                dp[i] += dp[i-2]

        return dp[-1]


s = Solution()
print(s.numDecodings("12"))
print(s.numDecodings("226"))
