# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid_pointer, end_pointer = head, head
        counter = 0
        while end_pointer.next:
            end_pointer = end_pointer.next
            counter += 1

        print(counter)
        counter = math.ceil(counter/2)
        while counter:
            mid_pointer = mid_pointer.next
            counter -= 1
        
        return mid_pointer
