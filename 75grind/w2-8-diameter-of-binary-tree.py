# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# failed to solve; revisit count: 1
class Solution:
    def __init__(self):
        self.diameter = 0

    def findDeepest(self, node: Optional[TreeNode]) -> int:
        """
        This function needs to do the following:
            1. Calculate the maximum depth of the left and right sides of the given node
            2. Determine the diameter at the given node and check if its the maximum
        """
        # Calculate maximum depth
        x = self.findDeepest(node.left) if node.left else 0
        y = self.findDeepest(node.right) if node.right else 0
        print('ini x y', x,y)
        # Calculate diameter
        if x + y > self.diameter:
            self.diameter = x + y
        # Make sure the parent node(s) get the correct depth from this node
        return 1 + (x if x > y else y)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.findDeepest(root)
        return self.diameter
root = TreeNode(1,TreeNode(2,TreeNode(4)),TreeNode(3))
x = Solution()
print(x.diameterOfBinaryTree(root))