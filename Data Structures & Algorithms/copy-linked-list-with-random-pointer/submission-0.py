"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        origin_copy = {None: None}
        curr = head

        while curr:
            copy = Node(curr.val)
            origin_copy[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = origin_copy[curr]
            copy.next = origin_copy[curr.next]
            copy.random = origin_copy[curr.random]
            curr = curr.next
        
        return origin_copy[head]