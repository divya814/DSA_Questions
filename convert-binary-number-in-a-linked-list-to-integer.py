# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if head==None or head.next==None:
            return head.val
        temp=head
        a=[]
        while temp!=None:
            a.append(temp.val)
            temp=temp.next
        ans=0
        j=len(a)-1
        for i in range(0,len(a)):
            ans+=(2**j)*a[i]
            j-=1
        return ans
