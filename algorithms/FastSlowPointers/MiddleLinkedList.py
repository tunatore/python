# Fast & Slow pointers

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# Time complexity O(N) and Space complexity O(1)
def find_middle_of_linked_list(head):
    if head is None:
        return None

    if head.next is None:
        return head

    slow = head
    fast = head.next

    while fast is not None:
        slow = slow.next
        if fast.next is not None:
            fast = fast.next.next
        else:
            fast = None
    return slow


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Middle Node: " + str(find_middle_of_linked_list(head).value))

    head.next.next.next.next.next = Node(6)
    print("Middle Node: " + str(find_middle_of_linked_list(head).value))

    head.next.next.next.next.next.next = Node(7)
    print("Middle Node: " + str(find_middle_of_linked_list(head).value))


main()
