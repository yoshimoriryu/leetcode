from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    # no brainer solution
    def cloneGraph1(self, node: Optional['Node']) -> Optional['Node']:
        new_node = deepcopy(node)
        return new_node

    # spec solution
    # failed to solve; use normal bfs, failed, must use recursion
    def helper(self, node, visited):
        if node is None:
            return None
        
        newNode = Node(node.val)
        visited[node.val] = newNode
        
        for adjNode in node.neighbors:
            if adjNode.val not in visited:
                newNode.neighbors.append(self.helper(adjNode, visited))
            else:
                newNode.neighbors.append(visited[adjNode.val])
        
        return newNode
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.helper(node, {})