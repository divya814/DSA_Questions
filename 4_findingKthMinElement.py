n=int(input())      // no. of elemeents
arr=list(map(int,input().split()))   //array
// kth minimum elemenent to find
k=int(input())
arr.sort()
print(arr[k-1])
