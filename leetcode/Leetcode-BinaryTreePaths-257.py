# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        if root is None:
            return None

        path = ""
        self.depth_first_recursive(root, path, paths)
        return paths

    def depth_first_recursive(self, root, path, paths):
        path += str(root.val)

        if root.left is None and root.right is None:
            paths.append(path)
            return

        if root.left is not None:
            self.depth_first_recursive(root.left, path + "->", paths)

        if root.right is not None:
            self.depth_first_recursive(root.right, path + "->", paths)


t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
t1.left.right = TreeNode(5)

s = Solution()
print(s.binaryTreePaths(t1))
