#include <iostream>
#include <climits>
using namespace std;

int main(){
    int n;
    cin>>n;
    int arr[n];
    for (int i=0;i<n;i++){
        cin>>arr[i];
    }
    int cursum=0;
    int maxSum=INT_MIN;
    for (int i=0;i<n;i++){
        cursum+=arr[i];
        if (cursum<0){
            cursum=0;
        }
        maxSum=max(cursum,maxSum);
    }
    if(maxSum==0){             //e.g. 4 -> -1 -2 -3 -4 
        maxSum=arr[0];
        for (int i=1;i<n;i++){
            maxSum=max(maxSum,arr[i]);        // maximum subarray is -1
    }
    }
    cout<<maxSum;
    return 0;
}
