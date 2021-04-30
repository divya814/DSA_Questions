# https://practice.geeksforgeeks.org/problems/word-break1352/1

def wordBreak(a,b):
    c=0
    res=""
    for i in a:
        res+=i
        if res in b:
            res=""
            c=1
        else:
            c=0
    return c
