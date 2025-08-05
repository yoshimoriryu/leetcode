class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.deepest(root)

    def deepest(self, root):
        if not root:
            return 0
        left = self.deepest(root.left)
        right = self.deepest(root.right)
        return 1 + (left if left > right else right)