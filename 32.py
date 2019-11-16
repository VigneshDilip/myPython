#THIS_CODE_IS_TO_REMOVE_LAST_ITEMS_IN_THE_DICTIONARY

#METHOD 1 USING POPITEM()
mydict={
"name":"dilip",
"branch":"ece",
"year":2020
}
print("old dict")
print(mydict)
print("new dict")
mydict.popitem()
print(mydict)
