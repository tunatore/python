class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if not 1 <= len(arr) <= 1000:
            return False

        d = dict([])

        for i in arr:
            if not -1000 <= i <= 1000:
                return False
            if i not in d:
                d[i] = 1
            else:
                d[i] = d[i] + 1

        if len(d.values()) == len(set(d.values())):
            return True
        else:
            return False