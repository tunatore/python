# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return None

        d = dict([])

        current = head

        while current is not None:
            if current.val not in d:
                d[current.val] = 1
                previous = current
                current = current.next
            else:
                if current.next is None:
                    previous.next = None
                    current = None
                else:
                    next_item = current.next
                    if next_item.val in d:
                        while next_item not in d:
                            current = next_item
                            break
                    else:
                        previous.next = next_item
                        current = next_item
                        previous = current
        return head

    def display_linkedlist(self, head):
        current = head
        while current is not None:
            print(current.val)
            current = current.next


# node1 = ListNode(1)
# node2 = ListNode(1)
# node3 = ListNode(2)
# node4 = ListNode(3)
# node5 = ListNode(3)
#
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(1)

node1.next = node2
node2.next = node3

s = Solution()
print(s.display_linkedlist(s.deleteDuplicates(node1)))
