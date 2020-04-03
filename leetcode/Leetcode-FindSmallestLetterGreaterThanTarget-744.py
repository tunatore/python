class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        if letters is None or not 2 <= len(letters) <= 10000 or target is None or not target.islower():
            return None

        return binary_search(letters, 0, len(letters), target)


def binary_search(letters, start, end, target):
    if start < end:
        mid = (start + end) // 2
        if ord(target) < ord(letters[mid]):
            return binary_search(letters, start, mid, target)
        elif ord(target) > ord(letters[mid]):
            return binary_search(letters, mid + 1, end, target)
        elif ord(target) == ord(letters[mid]):
            if mid + 1 <= len(letters) - 1:
                if ord(target) == ord(letters[mid]):
                    return binary_search(letters, mid + 1, end, target)
                else:
                    return letters[mid+1]
            else:
                return letters[0]

    if end >= len(letters): # if letter greater than all elements in list
        return letters[0]
    elif ord(target) < ord(letters[end]):  # if letter is less than last element
        return letters[end]
    else:
        return letters[0]  # if letter is less than all elements


s = Solution()
letters = ["c", "f", "j"]
print(s.nextGreatestLetter(letters, "a")) # c
print(s.nextGreatestLetter(letters, "c")) # f
print(s.nextGreatestLetter(letters, "d")) # f
print(s.nextGreatestLetter(letters, "g")) # j
print(s.nextGreatestLetter(letters, "j")) # c
print(s.nextGreatestLetter(letters, "k")) # c
letters = ["e","e","e","e","e","e","n","n","n","n"]
print(s.nextGreatestLetter(letters, "n"))