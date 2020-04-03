# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque

        if root is None:
            return

        q = deque()
        q.append(root)

        result = []
        result.append([root.val])

        while not len(q) == 0:
            nodes_count = len(q)
            level_nodes = []
            while nodes_count != 0:  # for each node in the level
                node = q.popleft()
                if node.left is not None:
                    level_nodes.append(node.left.val)
                    q.append(node.left)
                if node.right is not None:
                    level_nodes.append(node.right.val)
                    q.append(node.right)
                nodes_count -= 1
            if not len(level_nodes) == 0:
                result.insert(0, level_nodes)
        return result


t1 = TreeNode(3)
t1.left = TreeNode(9)
t1.right = TreeNode(20)
t1.right.left = TreeNode(15)
t1.left.right = TreeNode(7)

s = Solution()
print(s.levelOrderBottom(t1))