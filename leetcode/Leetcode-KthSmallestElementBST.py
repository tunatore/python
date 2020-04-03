# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        smallest = [0, 0]
        self.findkthSmallest(root, smallest, k)
        return smallest[1]

    def findkthSmallest(self, root, smallest, k):
        if root is None:
            return

        self.findkthSmallest(root.left, smallest, k)

        smallest[0] += 1
        if smallest[0] == k:
            smallest[1] = root.val
            return

        self.findkthSmallest(root.right, smallest, k)


t1 = TreeNode(3)
t1.left = TreeNode(1)
t1.right = TreeNode(4)
t1.left.right = TreeNode(2)

t2 = TreeNode(5)
t2.left = TreeNode(3)
t2.left.right = TreeNode(4)
t2.right = TreeNode(6)
t2.left.left = TreeNode(2)
t2.left.left.left = TreeNode(1)

s = Solution()
print(s.kthSmallest(t1, 1))
print(s.kthSmallest(t2, 3))
