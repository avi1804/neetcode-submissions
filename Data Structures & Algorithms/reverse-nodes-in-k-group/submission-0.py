class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        node = head
        for _ in range(k):
            if not node:
                return head
            node = node.next

        prev = None
        curr = head
        for _ in range(k):
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        head.next = self.reverseKGroup(curr, k)

        return prev  