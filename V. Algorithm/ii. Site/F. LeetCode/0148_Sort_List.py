# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        lst: List = []
        while p:
            lst.append(p.val)
            p = p.next
        lst.sort()
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head
        
