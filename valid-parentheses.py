# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if len(s)==1:
            return False
        for i in s:
            if i=="(" or i=="{" or i=="[":
                stack.append(i)
            elif len(stack)>0 and (i==")" or i=="]" or i=="}"):
                a=stack[-1]
                if (a=="(" and i==")") or (a=="[" and i=="]") or (a=="{" and i=="}"):
                    stack.pop()
                    
                else:
                    return False
            else:
                stack.append(i)
                break
                
        return len(stack)==0
        
