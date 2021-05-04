# https://leetcode.com/problems/linked-list-cycle-ii/

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return None
        a=head
        b=head
        while b and b.next:
            a=a.next
            b=b.next.next
            if a==b:
                break
        if a==b:
            while b!=head:
                b=b.next
                head=head.next
            return head
        else:
            return None
