friends=["Dilip","Vignesh","Esarapu","Disha","Patani"]
numbers=[1,2,3,4,5]
friends.extend(numbers)

friends.append("new element")  #to add a new element into the list
print(friends)
friends.insert(2,"YO") #to insert at a particular position

friends.remove("Esarapu") #removes the element "Esarapu"
print(friends)


friends.pop() #removes the last element in the list
print(friends)
friends.clear() #makes the list empty
print(friends)
