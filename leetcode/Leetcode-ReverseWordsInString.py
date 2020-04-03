class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        s.strip()
        split = s.split(' ');

        reverse = ""
        for i in range(len(split) - 1, -1, -1):
            reverse += split[i] + " "

        return ' '.join(reverse.strip().split())
        