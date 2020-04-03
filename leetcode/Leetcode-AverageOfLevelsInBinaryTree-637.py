from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        if root is None:
            return None

        q = deque()
        q.append(root)
        list_avg = []

        while not len(q) == 0:  # while queue is not empty
            nodes_count = len(q)
            temp_sum = 0
            level_count = nodes_count
            while nodes_count != 0:  # for each node in the level
                node = q.popleft()
                temp_sum += node.val
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                nodes_count -= 1
            list_avg.append(temp_sum / float(level_count))
        return list_avg


t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.right.left = TreeNode(15)
t.right.right = TreeNode(7)

s = Solution()
print(s.averageOfLevels(t))
