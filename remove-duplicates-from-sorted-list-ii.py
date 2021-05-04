# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:       
        if head==None or head.next==None :
            return head
        
        dummy=ListNode(0)
        prev=dummy
        
        while head:
            if head.next!=None and head.val==head.next.val:
                while head.next!=None and head.val==head.next.val:
                    head=head.next
            else:
                prev.next=head
                prev=prev.next
            head=head.next
            
        prev.next=None
        return dummy.next
        
