from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        final = self.levelOrder(root)
        final.sort()
        return final[k-1]
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        res = []
        q = deque()
        if root:
            q.append(root)

        while q:
            for i in range(len(q)):
                node = q.popleft()
                res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        print(res)
        return res