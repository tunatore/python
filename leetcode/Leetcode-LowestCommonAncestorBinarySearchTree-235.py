# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


t1 = TreeNode(3)
t1.left = TreeNode(5)
t1.right = TreeNode(1)
t1.right.left = TreeNode(0)
t1.right.right = TreeNode(8)
t1.left.right = TreeNode(2)
t1.left.left = TreeNode(6)
t1.left.right.right = TreeNode(4)
t1.left.right.left = TreeNode(7)


s = Solution()
print(s.lowestCommonAncestor(t1, TreeNode(5), TreeNode(1)).val)