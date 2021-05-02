# https://practice.geeksforgeeks.org/problems/next-permutation5226/1

# My solution (not passing all test cases)
'''
class Solution:
    def nextPermutation(self, N, arr):
        a=arr[:]
        a.sort(reverse=True)
        if arr==a:
            return sorted(arr)
        m1=max(arr)
        a1=[]
        k=arr.index(m1)
        e=arr[k-1]
        n=0
        b=[]
        for i in range(k-1,N):
            if arr[i]>e:
                b.append(arr[i])
        n=min(b)
        second=arr.index(n)
        arr[k-1],arr[second]=arr[second],arr[k-1]
        a1=arr[0:k]
        a1.extend(sorted(arr[k:N]))
        return a1[:]
 '''
