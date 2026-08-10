from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length_LL = 0
        cur = head
        while cur:
            length_LL += 1
            cur = cur.next

        prev, cur = 1, 1
        for i in range(1, length_LL + 1):
            if i % k == 0:
                head = self.reverseBetween(head, prev, i)
                prev = i + 1

        return head

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftPrev, cur = dummy, head
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next

        prev = None
        for i in range(right - left + 1):
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp

        leftPrev.next.next = cur
        leftPrev.next = prev
        return dummy.next
