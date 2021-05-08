# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1 or n==7:
            return True       
        s=str(n)
        while len(s)>1:
            a=0
            for i in range(0,len(s)):
                a+=int(s[i])**2
            s=str(a)
            if a==1 or a==7:
                return True
                break
        return False
