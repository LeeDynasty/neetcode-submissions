# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowptr = head
        fastptr = None
        if head is not None and head.next is not None and head.next.next is not None:
            fastptr = head.next.next
        else:
            return False

        while(slowptr is not fastptr):
            slowptr = slowptr.next 
            if fastptr.next is not None and fastptr.next.next is not None:
                fastptr = fastptr.next.next
            else:
                return False
        
        return True