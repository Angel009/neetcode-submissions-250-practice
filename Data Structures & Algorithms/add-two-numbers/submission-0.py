# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            curr = head
            prev = None

            len_list = 0

            while curr:
                len_list += 1
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            
            return prev, len_list
        
        l1_rev, l1_len = reverse(l1)
        l2_rev, l2_len = reverse(l2)

        num_sum = 0

        while l1_rev and l2_rev:
            num_sum += (l1_rev.val * (10 ** l1_len)) + (l2_rev.val * (10 ** l2_len))
            l1_rev = l1_rev.next
            l2_rev = l2_rev.next
            l1_len -= 1
            l2_len -= 1
        
        while l1_rev:
            num_sum += (l1_rev.val * (10 ** l1_len))
            l1_rev = l1_rev.next
            l1_len -= 1
        
        while l2_rev:
            num_sum += (l2_rev.val * (10 ** l2_len))
            l2_rev = l2_rev.next
            l2_len -= 1
        
        num_sum = str(num_sum // 10)

        extra_node = ListNode(0)
        curr = extra_node
        for i in range(len(num_sum)):
            sum_node = ListNode(int(num_sum[i]))
            curr.next = sum_node
            curr = curr.next

        ans, ans_len = reverse(extra_node.next)

        return ans       





