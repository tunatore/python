# fast slow pointers

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# Time complexity O(N) and Space complexity O(1)
def is_palindromic_linked_list(head):
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

    middle = slow

    # reverse second part
    reversed_second_part = reverse(middle.next)
    current = head

    reversed_pointer = reversed_second_part
    palindrome = True
    while current is not None and reversed_pointer is not None:
        if current.value == reversed_pointer.value:
            current = current.next
            reversed_pointer = reversed_pointer.next
        else:
            palindrome = False
            break

    # reverse again
    middle.next = reverse(reversed_second_part)
    return palindrome


# Time complexity O(N) and Space complexity O(1)
def reverse(head):
    previous = None
    current = head
    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous


def print_values(head):
    if head is None:
        print("LinkedList has no values")
    else:
        node = head
        while node is not None:
            print(node.value, "->", end="")
            node = node.next
        print()


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print_values(head)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))
    print_values(head)

    head.next.next.next.next.next = Node(2)

    print_values(head)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))
    print_values(head)


main()







