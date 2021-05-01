# https://practice.geeksforgeeks.org/problems/longest-prefix-suffix2527/1#

# My solution which is correct but giving TLE

class Solution:
	def lps(self, a):
		l=len(a)
		m=""
		if l==1:
		    return 0
		for j in range(0,l-1):
		    b=a[0:j+1]
		    c=a[l-j-1:]
            if b==c:
                m=b
		    
		return len(m)
    
    
# Solution provided in editorial, but giving wrong o/p for test case-"kkkk" as 2

def longestPrefixSuffix(s) :
    n = len(s)
    
    for res in range(n // 2, 0, -1) :
        prefix = s[0: res]
        suffix = s[n - res: n]
        
        if (prefix == suffix) :
            return res
    
    return 0
