class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# O(N) Time complexity and O(1) Space complexity
def has_cycle(head):

    if head is None or head.next is None:
        return None

    slow = head
    fast = head

    while fast is not None:
        slow = slow.next
        if fast.next is not None:
            fast = fast.next.next
        else:
            fast = None
        if slow == fast:
            return True
    return False


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))  # True

    head.next.next.next.next.next.next = head.next.next.next  # True
    print("LinkedList has cycle: " + str(has_cycle(head)))


main()
