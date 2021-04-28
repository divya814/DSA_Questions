# https://leetcode.com/problems/add-two-numbers/

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=ListNode()
        curr=head
        sumNode=0
        
        while l1 or l2 or sumNode:
            if l1:
                sumNode+=l1.val
                l1=l1.next
            if l2:
                sumNode+=l2.val
                l2=l2.next
            
            curr.next=ListNode(sumNode%10)
            sumNode//=10
            curr=curr.next
        
        return head.next
