# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        while i<len(t) and j<len(s):
            if t[i]==s[j]:
                j+=1
                i+=1
            else:
                i+=1
        if j==len(s):
            return True
        else:
            return False
        
