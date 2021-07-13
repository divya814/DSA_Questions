# Print minimum and maximum element in an array

class pair:
    def __init__(self):
        self.minE=0;
        self.maxE=0;

def minmax(a):
    num=pair()
    if len(a)==1:
        num.minE=a[0]
        num.maxE=a[0]
        return num
    num.minE=a[0]
    num.maxE=a[0]
    for i in range(0,len(a)):
        if a[i]<num.minE:
            num.minE=a[i]
        if a[i]>num.maxE:
            num.maxE=a[i]
    return num

a=[2,1,3,5,4,6,334,43535,4,36,46,35,46,575,67568]
k=minmax(a)
print(k.minE)
print(k.maxE)
