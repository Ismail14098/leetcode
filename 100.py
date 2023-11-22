# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def recursion(p, q):
            if p == None and q == None:
                return True
            elif p and q:
                return p.val == q.val and recursion(p.left, q.left) and recursion(p.right, q.right)
            else:
                return False
        return recursion(p, q)