from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        preorder = deque(preorder)

        root = TreeNode(preorder[0])
#       we know everything to the left of this root node is on the left side of the tree due to in order. Therefore
#       nodes right of the root is to the right of this selected node.
        middle = inorder.index(preorder[0])
        left, right = inorder[:middle], inorder[middle + 1:]
        print(middle, left, right)

        def build(preorder, inorder):
            if inorder:
                idx = inorder.index(preorder.popleft())
                root = TreeNode(inorder[idx])

                root.left = build(preorder, inorder[:idx])
                root.right = build(preorder, inorder[idx + 1:])

                return root

        return build(preorder, inorder)