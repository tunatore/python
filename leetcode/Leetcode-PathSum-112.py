# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        return self.dfs(root, sum, 0, False)

    def dfs(self, root, sum, tree_sum, result):
        tree_sum += root.val
        if root.left is None and root.right is None:
            if tree_sum == sum:
                result = True
                return result
            else:
                return False

        if root.left is not None and result is False:
            result = self.dfs(root.left, sum, tree_sum, result)

        if root.right is not None and result is False:
            result = self.dfs(root.right, sum, tree_sum, result)

        return result


t1 = TreeNode(5)
t1.left = TreeNode(4)
t1.left.left = TreeNode(11)
t1.left.left.left = TreeNode(7)
t1.left.left.right = TreeNode(2)
t1.right = TreeNode(8)
t1.right.left = TreeNode(23)
t1.right.right = TreeNode(4)
t1.right.right.right = TreeNode(1)

s = Solution()
print(s.hasPathSum(t1, 22))
