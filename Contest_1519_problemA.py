# https://codeforces.com/contest/1519/problem/A

def check(r,b,d):
    m=max(r,b)
    n=min(r,b)
    if abs(r-b)/n<=d:
        return "YES"
    else:
        return "NO"


t=int(input())
for i in range(t):
    rbd=list(map(int,input().split(" ")))
    print(check(rbd[0],rbd[1],rbd[2]))
