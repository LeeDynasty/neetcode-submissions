# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        # Find midpoint to split list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Reverse list for right side
        reversehead = slow
        prevptr = slow
        currptr = slow.next
        prevptr.next = None

        while currptr is not None:
            reversehead = currptr
            nextptr = currptr.next
            currptr.next = prevptr
            prevptr = currptr
            currptr = nextptr
            
        # Put together merged list- 1 ptr at head, 1 ptr at reversehead
        currptr1 = head
        currptr2 = reversehead

        while currptr2 is not slow and currptr1 is not slow:
            ptr1next = currptr1.next if currptr1.next is not None else None
            ptr2next = currptr2.next if currptr2.next is not None else None
            currptr1.next = currptr2
            currptr2.next = ptr1next

            currptr1 = ptr1next
            currptr2 = ptr2next
        return