# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = True
        def recursion(root: Optional[TreeNode]) -> int:
            nonlocal result
            if root is None:
                return 0
            l = recursion(root.left)
            r = recursion(root.right) 
            if abs(r-l) > 1:
                result = False
            return max(r, l)+1
        recursion(root)
        return result
        