# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy=ListNode(0)   
        temp=dummy
        carry=0
        while l1 and l2:
            s=l1.val+l2.val+carry            
            if s>9:
                carry=s//10
            else:
                carry=0
            temp.next=ListNode(s%10)
            temp=temp.next
            l1=l1.next
            l2=l2.next
            
        while l1:
            s=l1.val+carry            
            if s>9:
                carry=s//10
            else:
                carry=0
            temp.next=ListNode(s%10)
            temp=temp.next
            l1=l1.next
            
        while l2:
            s=l2.val+carry            
            if s>9:
                carry=s//10
            else:
                carry=0
            temp.next=ListNode(s%10)
            temp=temp.next
            l2=l2.next
            
        if carry!=0:
            temp.next=ListNode(carry)
            temp=temp.next
            
        return dummy.next
        
