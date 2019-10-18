friends=["Dilip","Vignesh","Esarapu","Disha","Patani"]
numbers=[100,2,37,4000000,5]
friends.extend(numbers)

print(friends.index("Vignesh"))
#An error pops up if we search for the elemt  which isnt in the list
print(friends.count("Dilip"))
numbers.sort()
print(numbers)
numbers.reverse() #to reverse the elements in the list
print(numbers)
numbersnew=numbers.copy() #to copy the lost to another new list
