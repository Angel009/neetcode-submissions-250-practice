# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        next_node = ListNode(0, head)
        prev_k = next_node

        while True:
            kth = self.getKth(prev_k, k)
            if not kth:
                break
            next_k = kth.next

            prev = kth.next
            curr = prev_k.next

            while curr != next_k:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = prev_k.next
            prev_k.next = kth
            prev_k = tmp
        return next_node.next