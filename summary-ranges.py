# https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        a=[]
        i=0
        l=len(nums)
        while i<l:
            seq=str(nums[i])
            j=i+1
            while j<l and nums[j]-nums[j-1]==1:
                j+=1
            
            if j-i>1:
                a.append(seq+"->"+str(nums[j-1]))
            else:
                a.append(seq)
            i=j
        return a
