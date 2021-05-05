# https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        while n!=1:
            if n%2!=0:
                return False
            else:
                n/=2           
            
        return True
      
# OR
return n>0 && ((n&(n-1)) == 0)
        
