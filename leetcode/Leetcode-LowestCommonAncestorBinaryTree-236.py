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
        paths1, paths2 = [], []
        if root is None:
            return None

        path = ""
        self.depth_first_recursive_path(root, p, path, paths1)
        self.depth_first_recursive_path(root, q, path, paths2)

        i, j, intersection_element = 0, 0, 0
        while i < len(paths1) and j < len(paths2):
            if paths1[i] == paths2[j]:
                intersection_element = i
            i += 1
            j += 1

        if len(paths1) > len(paths2):
            return self.find_node(root, int(paths2[intersection_element]))
        else:
            return self.find_node(root, int(paths1[intersection_element]))

    def find_node(self, root, n):
        if root is None:
            return None
        if root.val == n:
            return root

        left = self.find_node(root.left, n)
        right = self.find_node(root.right, n)

        if left is None:
            return right
        else:
            return left

    def depth_first_recursive_path(self, root, n, path, paths):
        path += str(root.val)

        if root.val == n.val:
            paths.extend(path.split(","))
            return

        if root.left is not None:
            self.depth_first_recursive_path(root.left, n, path + ",", paths)

        if root.right is not None:
            self.depth_first_recursive_path(root.right, n, path + ",", paths)


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
print(s.lowestCommonAncestor(t1, t1.left.right, t1.left.right.right).val)  # 2

t2 = TreeNode(1)
t2.left = TreeNode(2)
t2.right = TreeNode(3)
t2.left.right = TreeNode(4)

print(s.lowestCommonAncestor(t2, t2.left.right, t2).val)  # 1

t3 = TreeNode(-1)
t3.left = TreeNode(0)
t3.right = TreeNode(3)
t3.left.right = TreeNode(4)
t3.left.left = TreeNode(-2)
t3.left.left.left = TreeNode(8)

print(s.lowestCommonAncestor(t3, t3.left.left.left, t3.left.right).val)  # 0
print(s.lowestCommonAncestor(t3, t3, t3.left.left.left).val)  # -1
