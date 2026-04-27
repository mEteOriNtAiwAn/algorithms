    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        rev = slow.next
        slow.next = None
        pred = None

        while rev:
            temp = rev.next
            rev.next = pred
            pred = rev
            rev = temp

        first = head
        second = pred

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first,second = temp1, temp2

        