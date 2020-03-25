class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def is_palindrome1(node):
    palindrome_str = ""
    while node:
        palindrome_str += str(node.val)
        node = node.next
    return palindrome_str == palindrome_str[::-1]


def is_palindrome2(node):

    previous_nodes = []
    index = 0

    current_node = node
    while current_node:
        previous_nodes.append(current_node)
        current_node = current_node.next
        index += 1

    iteration_index = 1
    while iteration_index < index // 2:
        if previous_nodes[-iteration_index].val != node.val:
            return False
        node = node.next
        iteration_index += 1
    return True


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(2)
node6 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

print(is_palindrome1(node1))
print(is_palindrome2(node1))
