# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        prv=None
        while(current):
            nxt=current.next
            current.next=prv
            prv=current
            current=nxt
        return prv

    def printAnswer(self, answer):
        print(answer)

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3)))
    x = Solution()
    x.printAnswer(x.reverseList(head))
