# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.diameter = 0  # stores the maximum diameter calculated

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDepth(root)
        return self.diameter

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        self.diameter = max(self.diameter, left + right)

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))