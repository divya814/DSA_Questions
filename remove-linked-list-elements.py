# https://leetcode.com/problems/remove-linked-list-elements/

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head==None:
            return head
        curr=head
        prev=None
        while curr:
            if curr.val==val:
                if curr==head:
                    head=head.next
                    curr=head
                else:
                    prev.next=curr.next
                    curr=prev.next
            else:
                prev=curr
                curr=curr.next
        return head

    
# OR
        if head==None:
            return head
        head.next=self.removeElements(head.next,val)
        if head.val==val:
            head=head.next
        
        return head
