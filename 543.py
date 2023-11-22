# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        width = 0
        def recursion(root: Optional[TreeNode]) -> int:
            nonlocal width
            if root is None:
                return 0
            r = recursion(root.right)
            l = recursion(root.left)
            width = max(width, l+r)
            return max(l, r)+1
        recursion(root)
        return width