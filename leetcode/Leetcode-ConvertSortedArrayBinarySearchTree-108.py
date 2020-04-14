# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if nums is None or len(nums) == 0:
            return None

        return self.array_to_bst(nums, 0, len(nums) - 1)

    def array_to_bst(self, nums, start, end):
        if start > end:
            return None

        mid = (start + end) // 2
        tree_node = TreeNode(nums[mid])
        tree_node.left = self.array_to_bst(nums, start, mid - 1)
        tree_node.right = self.array_to_bst(nums, mid + 1, end)
        return tree_node


s = Solution()
print(s.sortedArrayToBST([-10, -3, 0, 5, 9]))
