# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        t=""
        m=""
        for i in range(len(s)):
            t+=s[i]
            for j in range(len(t)):
                if t[j]==s[i] and s[j:i+1]==s[j:i+1][::-1] and len(s[j:i+1])>len(m):
                    m=s[j:i+1]
                    break
                
        return m
                
        
