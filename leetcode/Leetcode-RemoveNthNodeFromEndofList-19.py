# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        d = dict([])
        nth_node_index = 0
        fast_node_index = 0

        current = head
        while current is not None:
            d[fast_node_index] = current
            if fast_node_index - nth_node_index < n:
                fast_node_index += 1
            elif fast_node_index - nth_node_index > n:
                nth_node_index += 1
                if current.next is not None:
                    fast_node_index += 1
            else:
                nth_node_index += 1
                fast_node_index += 1
            current = current.next

        if len(d) == 1:
            return None

        if len(d) > 1:
            del d[nth_node_index]

        i = 0
        last = None
        for key, node in d.items():
            if i == 0:
                head = ListNode(node.val)
                last = head
                i += 1
            else:
                last.next = ListNode(node.val)
                last = last.next
            print(node.val, end="->")
        return head


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
# node4 = ListNode(4)
# node5 = ListNode(5)

node1.next = node2
node2.next = node3
#node3.next = node4
# node4.next = node5

s = Solution()
s.removeNthFromEnd(node1, 3)
