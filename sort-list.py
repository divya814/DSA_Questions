# https://leetcode.com/problems/sort-list/ 

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        a.sort()
        curr=dummy=ListNode(0)
        for i in a:
            curr.next=ListNode(i)
            curr=curr.next
        return dummy.next
            
            
            
