#THIS_CODE_IS_TO_REMOVE_ITEMS_IN_THE_DICTIONARY

#METHOD 1 USING del
mydict={
"name":"dilip",
"branch":"ece",
"year":2020
}
print("old dict")
print(mydict)
print("new dict")
del mydict["branch"]
print(mydict)
