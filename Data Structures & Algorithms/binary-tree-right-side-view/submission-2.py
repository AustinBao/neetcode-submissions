from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        result = self.levelOrder(root)
        final = []
        for levels in result:
            last_node =  levels.pop()
            final.append(last_node)
        return final

    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        res = []
        q = deque()
        if root:
            q.append(root)

        while q:
            val = []

            for i in range(len(q)):
                node = q.popleft()
                val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(val)
        return res