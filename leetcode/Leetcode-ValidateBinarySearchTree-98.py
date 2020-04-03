# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.validate_tree(root, float('-inf'), float('inf'))

    def validate_tree(self, root, left_bound, right_bound):
        if root is None:
            return True

        return left_bound < root.val < right_bound \
               and self.validate_tree(root.left, left_bound, root.val) \
               and self.validate_tree(root.right, root.val, right_bound)


t1 = TreeNode(10)
t1.left = TreeNode(5)
t1.right = TreeNode(15)
t1.right.left = TreeNode(6)
t1.right.right = TreeNode(20)

s = Solution()
print(s.isValidBST(t1))
