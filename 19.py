def multiplyList(myList) : 
      
   
    mul = 1
    for x in myList: 
         mul = mul * x  
    return mul  
      
# Driver code 
list1 = [1, 2, 3]  
list2 = [3, 2, 4] 
print(multiplyList(list1)) 
print(multiplyList(list2)) 
