# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        is_balanced = [1]
        self.isBalancedMine(root, is_balanced)
        return is_balanced[0]
    
    def isBalancedMine(self, root, is_balanced):
        l_depth, r_depth = [0], [0]

        self.checkDeepest(root.left, 0, l_depth)
        self.checkDeepest(root.right, 0, r_depth)
        lr_diff = abs(l_depth[0] - r_depth[0])

        if lr_diff >  1:
            is_balanced[0] = 0
        else:
            if root.left:
                self.isBalancedMine(root.left, is_balanced)
            if root.right:
                self.isBalancedMine(root.right, is_balanced)

    def checkDeepest(self, root, depth, max_depth):
        if root:
            depth += 1
            self.checkDeepest(root.left, depth, max_depth)
            if depth > max_depth[0]:
                max_depth[0] = depth
            self.checkDeepest(root.right, depth, max_depth)


#########3 cool solution alert
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return (self.Height(root) >= 0)
    def Height(self, root: Optional[TreeNode]) -> bool:
        if root is None:  return 0
        leftheight, rightheight = self.Height(root.left), self.Height(root.right)
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:  return -1
        return max(leftheight, rightheight) + 1
