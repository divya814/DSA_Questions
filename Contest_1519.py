# https://codeforces.com/contest/1519/problem/A

def check(r,b,d):
    n=min(r,b)
    if abs(r-b)/n<=d:
        return "YES"
    else:
        return "NO"


t=int(input())
for i in range(t):
    rbd=list(map(int,input().split(" ")))
    print(check(rbd[0],rbd[1],rbd[2]))


# Problem B

def check(n,m,k):
    x=1
    y=1
    c=0
    while x!=n or y!=m:
        if x<n:
            x+=1
            c+=y
        if y<m:
            y+=1
            c+=x
    
    if c==k:
        return "YES"
    else:
        return "NO"
        
t=int(input())
for i in range(t):
    nmk=list(map(int,input().split(" ")))
    print(check(nmk[0],nmk[1],nmk[2]))
