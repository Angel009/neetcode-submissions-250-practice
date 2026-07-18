"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_new = {}

        def clone(node):
            if node in old_new:
                return old_new[node]
            
            copy = Node(node.val)
            old_new[node] = copy

            for new in node.neighbors:
                copy.neighbors.append(clone(new))
            
            return copy
        
        return clone(node) if node else None

