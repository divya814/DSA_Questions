# https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy=new=ListNode(0)
        tail=newhead=ListNode(0)        
        temp=head
        
        while temp:
            if temp.val<x:
                new.next=temp
                new=new.next
            else:
                tail.next=temp
                tail=tail.next
            temp=temp.next
            
        tail.next=None
        new.next=newhead.next
        
        return dummy.next
        
