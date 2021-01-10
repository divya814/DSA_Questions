S=input()
n=len(S)
check=1      # flag
for i in range(len(S)):
    if S[i]!=S[n-i-1]:
        check=0
if check==1:
    print("Is Pallindrome")
else:
    print("Not Pallindrome")
