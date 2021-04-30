# https://practice.geeksforgeeks.org/problems/edit-distance3702/1

class Solution:
	def editDistance(self, s, t):
	    m=len(s)
	    n=len(t)
	    d=[[0 for i in range(n+1)] for j in range(m+1)]
	    
	    for i in range(m+1):
	        for j in range(n+1):
	            if i==0:
	                d[i][j]=j
	            elif j==0:
	                d[i][j]=i
	            elif s[i-1]==t[j-1]:   # when same
	                d[i][j]=d[i-1][j-1]
	            else:   #if not same
	                d[i][j]=1+ min(d[i][j-1],d[i-1][j-1],d[i-1][j])
        return d[m][n]	      # last element in the table    
