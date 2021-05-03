# https://leetcode.com/problems/intersection-of-two-linked-lists/

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        n1=headA
        n2=headB
        a,b=0,0
        while n1:
            n1=n1.next
            a+=1
        while n2:
            n2=n2.next
            b+=1
        n1=headA
        n2=headB
        if a>b:
            i=a-b
            while i>0:
                n1=n1.next
                i-=1
        else:
            i=b-a
            while i>0:
                n2=n2.next
                i-=1
        while n1 or n2:
            if n1==n2:
                return n1
            n1=n1.next
            n2=n2.next           
        return None
        
        
# A better approach:
        d={}
        while headA:
            d[headA]=1
            headA=headA.next
        while headB:
            if headB in d:
                return headB
            headB=headB.next
        return None

        
