# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = None
        mergedlist_head = None
        list1ptr = list1
        list2ptr = list2

        if list1ptr is None:
            return list2ptr
        elif list2ptr is None:
            return list1ptr
        
        if list1ptr.val > list2ptr.val:
            mergedList = list2ptr
            list2ptr = list2ptr.next
        else:
            mergedList = list1ptr
            list1ptr = list1ptr.next

        mergedlist_head = mergedList

        while list1ptr is not None and list2ptr is not None:
            if list1ptr.val > list2ptr.val:
                mergedList.next = list2ptr
                mergedList = list2ptr
                list2ptr = list2ptr.next
            else:
                mergedList.next = list1ptr
                mergedList = list1ptr
                list1ptr = list1ptr.next
        
        if list1ptr is None and list2ptr is not None:
            mergedList.next = list2ptr
        elif list2ptr is None and list1ptr is not None:
            mergedList.next = list1ptr

        return mergedlist_head