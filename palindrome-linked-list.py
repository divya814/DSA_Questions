# https://leetcode.com/problems/palindrome-linked-list/

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        a=[]
        while head!=None:
            a.append(head.val)
            head=head.next
        if a[:]==a[::-1]:
            return True
        else:
            return False
