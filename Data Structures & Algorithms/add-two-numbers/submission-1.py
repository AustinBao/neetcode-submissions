from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1str = self.linkedToString(l1)
        l2str = self.linkedToString(l2)

        finalCalcInt = int(l1str) + int(l2str)

        return self.strToLinked(str(finalCalcInt)[::-1])

    def linkedToString(self, l1: Optional[ListNode]) -> str:
        curr = l1
        stringedNum = ""
        while curr:
            stringedNum += str(curr.val)
            curr = curr.next

        return stringedNum[::-1]

    def strToLinked(self, num: str) -> Optional[ListNode]:
        first = []
        for i in range(len(num)):
            newNode = ListNode(val=int(num[i]))
            first.append(newNode)

        for nodeIndex in range(len(first)):
            if nodeIndex == len(first) - 1:
                first[nodeIndex].next = None
            else:
                first[nodeIndex].next = first[nodeIndex + 1]

        return first[0]

            