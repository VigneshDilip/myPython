def largest(arr,n): 
  
    # Initialize maximum element 
    max = arr[0] 
  
    
    for i in range(1, n): 
        if arr[i] > max: 
            max = arr[i] 
    return max
  
 
arr = [100, 324, 49, 90, 9858] 
n = len(arr) 
Ans = largest(arr,n) 
print ("The largest element in the given array is ",Ans) 
