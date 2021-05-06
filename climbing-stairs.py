# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return n
        first=1
        sec=2
        for i in range(3,n+1):
            third=first+sec
            first=sec
            sec=third
        return sec
