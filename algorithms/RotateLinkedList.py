class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def rotate(node, k):
    if node is None or k is None or k <= 0:
        return node

    count = 1
    current = node
    while current and count < k:
        count += 1
        current = current.next

    rotated_next = current.next
    if rotated_next is None:
        return node
    current.next = None

    rotated_next_current = rotated_next
    while rotated_next_current:
        rotated_next_last = rotated_next_current
        rotated_next_current = rotated_next_current.next

    rotated_next_last.next = node
    return rotated_next


def display_linkedlist(head):
    current = head
    while current is not None:
        print(current.val, "->", end="")
        current = current.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

print(display_linkedlist(rotate(node1, 5)))