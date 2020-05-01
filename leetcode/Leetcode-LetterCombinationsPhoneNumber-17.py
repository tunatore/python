class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        letter_combinations = []
        if digits is None or len(digits) == 0:
            return letter_combinations

        mapping_phone_nums = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.recursive_letter_combination(letter_combinations, digits, mapping_phone_nums, current_combination='', index=0)
        return letter_combinations

    def recursive_letter_combination(self, letter_combinations, digits, mapping_phone_nums, current_combination, index):
        if index == len(digits):
            letter_combinations.append(current_combination)
            return

        letters = mapping_phone_nums[int(digits[index])]
        for i in range(len(letters)):
            self.recursive_letter_combination(letter_combinations,
                                              digits,
                                              mapping_phone_nums,
                                              current_combination + letters[i],
                                              index + 1)


s = Solution()
print(s.letterCombinations("1"))
print(s.letterCombinations("0"))
print(s.letterCombinations("23"))
print(s.letterCombinations("235"))

