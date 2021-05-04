# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if (len(s)==1 and s==" ") or s=="":
            return 0
        
        new_s  = s.strip(" ").split(" ")
        l=len(new_s[-1])
        return l
