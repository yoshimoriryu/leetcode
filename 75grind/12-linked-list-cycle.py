# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if not head.next:
            return False

        is_loop = False
        history = {}
        while head.next:
            if head in history:
                    is_loop = True
                    break
            else:
                history[head] = head.val
                head = head.next
        if not head:
            return False
        return is_loop
