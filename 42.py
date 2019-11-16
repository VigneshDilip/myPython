#TO_REVERSE_A_STRING
i=0
text="Hello World"
s=""
l=len(text)
for i in range(0,l):
  s=text[i]+s
print(s)
