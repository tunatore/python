# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        longest_consecutive_max = [0]
        count = 0
        target = 0
        self.findLongestConsecutive(root, count, target, longest_consecutive_max)
        return longest_consecutive_max[0]

    def findLongestConsecutive(self, root, count, target, longest_consecutive_max):
        if root is None:
            return
        elif root.val == target:
            count += 1
        else:
            count = 1

        longest_consecutive_max[0] = max(int(longest_consecutive_max[0]), count)
        self.findLongestConsecutive(root.left, count, root.val + 1, longest_consecutive_max)
        self.findLongestConsecutive(root.right, count, root.val + 1, longest_consecutive_max)


t1 = TreeNode(1)
t1.right = TreeNode(3)
t1.right.left = TreeNode(2)
t1.right.right = TreeNode(4)
t1.right.right.right = TreeNode(5)

t2 = TreeNode(2)
t2.right = TreeNode(3)
t2.right.left = TreeNode(2)
t2.right.left.left = TreeNode(1)

s = Solution()
print(s.longestConsecutive(t1))
print(s.longestConsecutive(t2))
