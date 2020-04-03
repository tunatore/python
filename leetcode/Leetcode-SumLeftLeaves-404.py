# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None or (root.left is None and root.right is None):
            return 0

        return self.depth_first_recursive(root)

    def depth_first_recursive(self, root):

        sum = 0
        if root.left is None and root.right is None:
            sum += root.val
            return sum

        if root.left is not None or (root.left is not None and root.left.left is None and root.left.right is None):
            sum += self.depth_first_recursive(root.left)

        if root.right is not None and (root.right.left is not None or root.right.right is not None):
            sum += self.depth_first_recursive(root.right)
        return sum


t1 = TreeNode(3)
t1.left = TreeNode(9)
t1.right = TreeNode(20)
t1.right.left = TreeNode(15)
t1.right.right = TreeNode(7)

t2 = TreeNode(1)
t2.left = TreeNode(2)
t2.right = TreeNode(3)
t2.left.left = TreeNode(4)
t2.left.right = TreeNode(5)

t3 = TreeNode(3)
t3.left = TreeNode(9)
t3.right = TreeNode(20)
t3.right.left = TreeNode(15)
t3.right.right = TreeNode(7)

s = Solution()
print(s.sumOfLeftLeaves(t1))
print(s.sumOfLeftLeaves(t2))
print(s.sumOfLeftLeaves(t3))