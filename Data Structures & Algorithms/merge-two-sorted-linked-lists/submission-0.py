# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1 # we are now telling the tail to point to the list1 value 
                list1 = list1.next #we are now moving the pointer in the list1 to the next value
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next # this is were we are moving the tail
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next

