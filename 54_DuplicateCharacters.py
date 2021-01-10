S=input()
n=len(S)

# make an array of size 256 for all no. of characters
check=[0]*256  

for i in S:
    check[ord(i)]+=1       # ord() gives ASCII value of chacters
    
k=0
for i in check:
    if int(i)>1:    
        print(chr(k)+" occurred "+str(i)+" times")
    k+=1
