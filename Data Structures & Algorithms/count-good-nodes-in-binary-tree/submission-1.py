class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)

    def dfs(self, root, maximum:int):
        if not root:
            return 0

        res = 1 if root.val >= maximum else 0

        newmax = max(root.val, maximum)

        left, right = self.dfs(root.left, newmax), self.dfs(root.right, newmax)

        return res + left + right
