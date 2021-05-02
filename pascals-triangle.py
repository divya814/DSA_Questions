# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, n: int) -> List[List[int]]:        
        l = []        
        for row in range(1,n+1):            
            p= [1]*(row)
            
            if len(p) >= 3:
                for pos in range(1, len(p)-1):
                    p[pos] = l[-1][pos-1] + l[-1][pos]
                
            l.append(p)            
        return l
