# fast - slow pointers
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


# Time complexity O(N) and Space complexity O(1)
def find_cycle_start(head):
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
            cycle_length = calculate_cycle_length(slow)
            break
    return find_start_cycle(head, cycle_length)


def calculate_cycle_length(slow):
    current = slow
    cycle_length = 0
    while current is not None:
        cycle_length += 1
        current = current.next
        if current == slow:
            break
    return cycle_length


def find_start_cycle(head, cycle_length):

    pointer1 = head
    pointer2 = head

    while cycle_length != 0:
        pointer2 = pointer2.next
        cycle_length -= 1

    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    # head.next.next.next.next.next.next = head.next.next.next
    # print("LinkedList cycle start: " + str(find_cycle_start(head).value))
    #
    # head.next.next.next.next.next.next = head
    # print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
