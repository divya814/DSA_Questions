# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=a[::-1]
        b=b[::-1]
        if len(a)>len(b):
            while len(b)!=len(a):
                b=b+'0'
        elif len(b)>len(a):
            while len(a)!=len(b):
                a=a+'0'
        s=""
        c=0
        for i in range(len(a)):

            if a[i]=="1" and b[i]=="1":
                if c==0:
                    s=s+"0"
                    c=1
                else:
                    s=s+"1"
                    c=1
            elif (a[i]=="1" and b[i]=="0") or (a[i]=="0" and b[i]=="1"):
                if c==0:
                    s=s+"1"
                    c=0
                else:
                    s=s+"0"
                    c=1
            elif a[i]=="0" and b[i]=="0":
                if c==1:
                    s=s+"1"
                    c=0
                else:
                    s=s+"0"
                    c=0
        if c==1:
            s=s+"1"
        s=s[::-1]
        return s
