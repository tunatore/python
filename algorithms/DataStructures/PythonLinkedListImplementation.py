class LinkedList:
    def __init__(self, node=None):
        self.head = node

    def next(self, next_item):
        new_node = ListNode(next_item)
        if self.head is not None:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def values(self):
        if self.head is None:
            print("LinkedList has no values")
        else:
            node = self.head
            while node is not None:
                print(node.get_data(), "->", end="")
                node = node.next

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous


class ListNode:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def data(self, data):
        self.data = data


node1 = ListNode(3)
l = LinkedList(node1)
l.next(3)
l.next(4)
l.next(5)
l.next(6)
l.values()
print()
l.next(7)
l.next(8)
l.values()
print()
l.reverse()
l.values()