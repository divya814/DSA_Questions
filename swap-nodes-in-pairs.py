# https://leetcode.com/problems/swap-nodes-in-pairs/

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        prev=head
        curr=head.next
        while curr:
            prev.val, curr.val=curr.val,prev.val
            if prev.next==None or curr.next==None:
                return head
            prev=curr.next
            curr=prev.next
        return head
