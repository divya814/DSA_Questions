# reversing the array using swap

n=int(input())
arr=list(map(int,input().split()))
st=0
en=n-1
while st<en:
    arr[st],arr[en]=arr[en],arr[st]
    st+=1
    en-=1
print(arr)


#or simple- arr[::-1]
