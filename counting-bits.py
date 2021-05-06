# https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, num: int) -> List[int]:
        dp=[0]*(num+1)
        for i in range(num+1):
            dp[i]=i%2 + dp[i//2]
        return dp
            
        
