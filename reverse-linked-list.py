# https://leetcode.com/problems/reverse-linked-list/

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev=None
        curr=head
        n=head
        while curr!=None:
            n=curr.next
            curr.next=prev
            prev=curr
            curr=n
            
        return prev
