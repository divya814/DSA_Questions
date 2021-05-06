# https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, a: List[int], queries: List[List[int]]) -> List[int]:
        x=[]
        for i in queries:
            l=i[0]
            r=i[1]
            k=a[l:r+1]
            s=0
            for j in k:
                s^=j
            x.append(s)
        return x
        
