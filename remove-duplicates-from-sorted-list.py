# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre=head
        if head==None or head.next==None :
            return head
        curr=pre.next
        while curr:
            if pre.val==curr.val:
                pre.next=curr.next
            else:
                pre=curr
            curr=curr.next
        return head
                
        
