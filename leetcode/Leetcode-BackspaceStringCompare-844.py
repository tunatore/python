class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        if not (1 <= len(S) <= 200 and 1 <= len(T) <= 200):
            return False

        return self.compare_str(S) == self.compare_str(T)

    def compare_str(self, str_arr):
        stack = []
        for i in range(len(str_arr)):
            if str_arr[i] == '#' and stack:
                stack.pop()
            elif str_arr[i] != '#':
                stack.append(str_arr[i])
        return stack


s = Solution()
# S = "ab#c"
# T = "ad#c"
# print(s.backspaceCompare(S, T))
# S = "ab##"
# T = "c#d#"
# print(s.backspaceCompare(S, T))
# S = "a##c"
# T = "#a#c"
# print(s.backspaceCompare(S, T))
# S = "a#c"
# T = "b"
# print(s.backspaceCompare(S, T))
S = "y#fo##f"
T = "y#f#o##f"
print(s.backspaceCompare(S, T))