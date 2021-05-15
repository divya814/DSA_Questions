# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head==None:
            return head
        
        dummy=newhead=ListNode(0)        
        t=head
        l=0
        temp=head
        while temp:
            temp=temp.next
            l+=1
        c=1
        k=k%l   # if k is greater than length of LL
        key=l-k        
        while t and c<key:
            t=t.next
            c+=1
        newhead.next=t.next   # head for new LL
        t.next=None    # end/tail of new LL
        
        while newhead.next:
            newhead=newhead.next
        newhead.next=head
        
        return dummy.next
            
        
