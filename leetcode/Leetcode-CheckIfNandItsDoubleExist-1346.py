class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if not 2 <= len(arr) <= 500:
            return False

        d = dict([])
        for i in arr:
            if not -10**3 <= i <= 10**3:
                return False
            if i not in d:
                d[i] = 1
            else:
                d[i] = d[i] + 1

        for key in d:
            num = key / float(2)
            if key == 0:
                if d[key] > 1:
                    return True
            else:
                if num in d:
                    return True
        return False