# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp=head
        c=0
        while temp!=None:
            temp=temp.next
            c+=1
            
        if c==n:
            return head.next
        
        k=c-n
        p=head
        i=1        
        while p.next:
            if i==k:
                p.next=p.next.next
            else:
                p=p.next
            i+=1            
        return head
