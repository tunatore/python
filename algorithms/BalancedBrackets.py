class Solution(object):
    def balanced_brackets(self, str):

        # left bracket
        open_bracket_list = ["{", "(", "["]

        # right bracket
        closed_bracket_list = ["}", ")", "]"]
        stack = []

        for char in str:

            # push bracket when it is left bracket
            if char in open_bracket_list:
                stack.append(char)
            # pop bracket when it is right bracket
            elif char in closed_bracket_list:
                closed_bracket_index = closed_bracket_list.index(char)
                if len(stack) > 0 and open_bracket_list[closed_bracket_index] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


s = Solution()
print("{}():", s.balanced_brackers("{}()"))
print("({()}):", s.balanced_brackers("({()})"))
print("{}(:", s.balanced_brackers("{}("))
print("[]:", s.balanced_brackers("[]"))
print("(:", s.balanced_brackers("("))
print("):", s.balanced_brackers(")"))
print(")]:", s.balanced_brackers(")]"))
print("()[{]}:", s.balanced_brackers("()[{]}"))
print("(){}[:", s.balanced_brackers("(){}["))