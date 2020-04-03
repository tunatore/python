# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if p is None and q is None:
            return True

        if p is not None and q is not None:
            if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                return True
        return False


treeNode1 = TreeNode(1)
treeNode1a = TreeNode(2)
treeNode1b = TreeNode(3)
treeNode1.left = treeNode1a
treeNode1.right = treeNode1b

treeNode2 = TreeNode(1)
treeNode2a = TreeNode(2)
treeNode2b = TreeNode(3)
treeNode2.left = treeNode2a
treeNode2.right = treeNode2b

s = Solution()
print(s.isSameTree(treeNode1, treeNode2))

