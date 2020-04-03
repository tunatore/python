class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        s_char_array = list(s)
        t_char_array = list(t)

        d = dict([])

        for c in t_char_array:
            if c not in d:
                d[c] = 1
            else:
                d[c] = d[c] + 1

        for c_t in s_char_array:
            if c_t not in d:
                return c_t
            else:
                d[c_t] = d[c_t] - 1

        res = list(dict((k, v) for k, v in d.items() if v == 1))
        if len(res) == 0:
            return ""
        else:
            return res[0]