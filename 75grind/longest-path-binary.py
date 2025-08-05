import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def longestPath(root):
    if root is None:
        return []
    rightvect = longestPath(root.right)
    leftvect = longestPath(root.left)
    if len(leftvect) > len(rightvect):
        leftvect.append(root.data)
    else:
        rightvect.append(root.data)
    return leftvect if len(leftvect) > len(rightvect) else rightvect

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)

output = longestPath(root)
print(" -> ".join(str(i) for i in output[::-1]))