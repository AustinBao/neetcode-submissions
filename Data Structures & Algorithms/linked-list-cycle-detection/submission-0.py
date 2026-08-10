# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        stack = []
        while curr:
            stack.append(curr)

            if curr.next is None:
                return False
            else:
                if curr.next in stack:
                    return True

            curr = curr.next

        return True
