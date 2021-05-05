# Finding odd times occuring element in the array 

def findOddMan(array):
  # Complete the given function
  # Return the element that occurs odd times
  k=max(array)
  c=[0]*(k+1)
  for i in range(len(array)):
    c[array[i]]+=1
    
  for i in range(1,len(c)):
    if c[i]%2>0:
      return i
