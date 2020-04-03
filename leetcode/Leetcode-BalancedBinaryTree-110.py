# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None or (root.left is None and root.right is None):
            return True

        balanced = self.depth_of_tree(root)
        return balanced != -1

    def depth_of_tree(self, root):  # height of binary search tree
        if root is None:
            return 0

        left_height = self.depth_of_tree(root.left)
        right_height = self.depth_of_tree(root.right)

        if left_height == -1 or right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)


t1 = TreeNode(3)
t1.left = TreeNode(9)
t1.right = TreeNode(20)
t1.right.left = TreeNode(15)
t1.right.right = TreeNode(7)

t2 = TreeNode(1)
t2.left = TreeNode(2)
t2.right = TreeNode(2)
t2.left.left = TreeNode(3)
t2.left.right = TreeNode(3)
t2.left.left.left = TreeNode(4)
t2.left.left.right = TreeNode(4)

t3 = TreeNode(1)
t3.left = TreeNode(2)
t3.right = TreeNode(2)
t3.left.left = TreeNode(3)
t3.right.right = TreeNode(3)
t3.left.left.left = TreeNode(4)
t3.right.right.right = TreeNode(4)

t4 = TreeNode(1)
t4.left = TreeNode(2)
t4.right = TreeNode(2)
t4.left.left = TreeNode(3)
t4.left.right = TreeNode(3)
t4.right.right = TreeNode(3)
t4.right.left = TreeNode(3)
t4.left.left.left = TreeNode(4)
t4.left.left.right = TreeNode(4)
t4.left.right.left = TreeNode(4)
t4.left.right.right = TreeNode(4)
t4.right.left.left = TreeNode(4)
t4.right.left.right = TreeNode(4)
t4.left.left.left.left = TreeNode(5)
t4.left.left.left.right = TreeNode(5)

s = Solution()
print(s.isBalanced(t1))
print(s.isBalanced(t2))
print(s.isBalanced(t3))
print(s.isBalanced(t4))
