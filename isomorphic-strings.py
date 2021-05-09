# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]]!=t[i]:
                    return False
            else:
                d[s[i]]=t[i] 
        
        if len(set(s))==len(set(t)):   
            return True
        return False
        
