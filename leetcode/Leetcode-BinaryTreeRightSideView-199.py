# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if root is None:
            return

        from collections import deque
        q = deque()
        q.append(root)

        result = []
        result.append(root.val)

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
                result.append(level_nodes[-1])
        return result


t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.right.right = TreeNode(4)
t.left.right = TreeNode(5)

# t = TreeNode(1)
# t.left = TreeNode(2)
# t.right = TreeNode(3)
# t.left.left = TreeNode(4)
s = Solution()
print(s.rightSideView(t))