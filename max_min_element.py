
arr=list(map(int,input().split()))
maximum=-99999
minimum=100000
for i in range(len(arr)):
    if maximum<arr[i]:
        maximum=arr[i]
print("maximum element= ",maximum)
for i in range(len(arr)):
    if minimum>arr[i]:
        minimum=arr[i]
print("minimum element= ",minimum)  
        
