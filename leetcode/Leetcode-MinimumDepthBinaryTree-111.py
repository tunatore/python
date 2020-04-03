# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        from collections import deque

        if root is None:
            return 0

        q = deque()
        q.append(root)
        level_count = 0

        while not len(q) == 0:  # while queue is not empty
            nodes_count = len(q)
            level_count += 1
            while nodes_count != 0:  # for each node in the level
                node = q.popleft()
                if node.left is None and node.right is None:
                    return level_count
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                nodes_count -= 1
        return level_count


t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.right.left = TreeNode(15)
t.right.right = TreeNode(7)

s = Solution()
print(s.minDepth(t))