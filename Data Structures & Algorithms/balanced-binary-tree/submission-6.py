# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            left = check(root.left)
            if left == -1:
                return -1  # left subtree is not balanced
            
            right = check(root.right)
            if right == -1:
                return -1  # right subtree is not balanced

            if abs(left - right) > 1:
                return -1  # current node is not balanced

            return 1 + max(left, right)  # return the height of the subtree

        return check(root) != -1

        
