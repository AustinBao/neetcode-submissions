from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = [root.val]

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            # to ensure we never add negative numbers
            left = max(left, 0)
            right = max(right, 0)

            maxsum[0] = max(maxsum[0], left + right + root.val)
            
            return root.val + max(left, right)
        
        dfs(root)
        return maxsum[0]
    