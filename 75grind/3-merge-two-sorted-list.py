# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # My own
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2:
            return list1
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        pointer = head
        while list1 and list2:
            if list1.val <= list2.val:
                pointer.next = list1
                pointer = pointer.next
                list1 = list1.next
            else:
                pointer.next = list2
                pointer = pointer.next
                list2 = list2.next

        if list1:
            pointer.next = list1
        if list2:
            pointer.next = list2

        return head
