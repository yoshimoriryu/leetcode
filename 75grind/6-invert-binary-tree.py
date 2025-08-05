from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertingTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invertingTree(root)
        return root
    def printAnswer(self, answer):
        print(answer)

if __name__ == "__main__":
    prices = TreeNode{val: 6, left: TreeNode{val: 2, left: TreeNode{val: 0, left: None, right: None}, right: TreeNode{val: 4, left: TreeNode{val: 3, left: None, right: None}, right: TreeNode{val: 5, left: None, right: None}}}, right: TreeNode{val: 8, left: TreeNode{val: 7, left: None, right: None}, right: TreeNode{val: 9, left: None, right: None}}}
    x = Solution()
    x.printAnswer(x.invertTree(prices))
