# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        temp = head
        cont_sum = 0
        while l1 or l2:
            if l1:
                cont_sum += l1.val
                l1 = l1.next
            if l2:
                cont_sum += l2.val
                l2 = l2.next
            
            new_node = ListNode(val=(cont_sum%10))
            temp.next = new_node
            temp = new_node
            cont_sum //= 10

        if cont_sum != 0:
            new_node = ListNode(val=cont_sum)
            temp.next = new_node

        return head.next

        
        