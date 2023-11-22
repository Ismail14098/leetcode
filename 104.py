class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recursion(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            return max(recursion(root.right), recursion(root.left))+1
        return recursion(root)