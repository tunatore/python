class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not 1 <= len(arr) <= 10 ** 4:
            return -1

        d = dict([])

        for i in arr:
            if not 0 <= i <= 10 ** 5:
                return False
            if i not in d:
                d[i] = 1
            else:
                d[i] = d[i] + 1

        times = len(arr) / 4

        dict_values = {key: value for (key, value) in d.items() if value > times}
        return list(dict_values)[0]