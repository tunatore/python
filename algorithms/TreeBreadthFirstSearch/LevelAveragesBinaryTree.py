from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# Time complexity O(N) and Space complexity O(N)
def find_level_averages(root):
    result = []
    if root is None:
        return None

    q = deque()
    q.append(root)

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
        result.append(temp_sum / float(level_count))
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))


main()







