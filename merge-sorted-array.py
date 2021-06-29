# https://leetcode.com/problems/merge-sorted-array/
# Merge 2 sorted arrays in 1st array
# Start merging from last
# check for the largest element in both the arrays and then send it in the end of nums1

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for p in range(m+n-1,-1,-1):
            if m and n and nums1[m-1]>nums2[n-1]:
                nums1[p]=nums1[m-1]
                m-=1
            elif n:
                nums1[p]=nums2[n-1]
                n-=1
        
            
    
