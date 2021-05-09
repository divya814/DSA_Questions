# https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:
            return 0
        prime=[0]*(n)
        for i in range(2,int(n**0.5)+1):  # or (2,n)
            for j in range(i*i,n,i):
                if prime[j]==0:
                    prime[j]=1
        c=0
        for i in range(2,n):
            if prime[i]==0:
                c+=1
        return c
