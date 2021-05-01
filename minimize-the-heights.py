# https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1#

class Solution:
    def getMinDiff(self, a, n, k):
        # code here
        a.sort()
        ans= a[n-1]-a[0]
        for i in range(1,n):
            if (a[i]<k):
                continue
            
            mini=min(a[0]+k,a[i]-k)
            maxi=max(a[n-1]-k,a[i-1]+k)
            ans=min(ans,maxi-mini)
        
        return ans
