from typing import Optional
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        queue = deque()

        for ll in lists:
            item_cur = ll
            while item_cur is not None:
                queue = self.enqueue_with_priority(queue, item_cur.val)
                item_cur = item_cur.next

        return self.queueIntoLL(queue)


    def enqueue_with_priority(self, queue, value):
        queue.append(value)
        queue = deque(sorted(queue))  # Sort after every insertion
        return queue


    def queueIntoLL(self, queue:deque) -> Optional[ListNode]:
        cur = dummy = ListNode(0)

        while len(queue) > 0:
            cur.next = ListNode(queue.popleft())
            cur = cur.next
        return dummy.next
    #
    # def lst2link(lst):
    #     cur = dummy = ListNode(0)
    #     for e in lst:
    #         cur.next = ListNode(e)
    #         cur = cur.next
    #     return dummy.next