# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Move forward n times with 1 pointer, and then we can move both pointers forward until we hit the end of the list. Then we can remove the offset pointer. For the offset pointer, we need to save the previous pointer so we can hook them up to current.next

        prevptr = None
        curptr = head
        endptr = head

        for i in range(n):
            endptr = endptr.next

        while endptr is not None:
            prevptr = curptr
            curptr = curptr.next
            endptr = endptr.next

        if prevptr is None:
            return curptr.next

        prevptr.next = curptr.next

        return head