# https://leetcode.com/problems/valid-number/

class Solution:
    def isNumber(self, s: str) -> bool:
        if s.count('inf')>0 or s.count('Infinity')>0: 
            return False
        try:
            float(s)
            return True
        except:
            return False
