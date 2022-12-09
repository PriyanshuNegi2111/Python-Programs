#Program to sort dictonary keys and values
a=eval(input("Enter the products dictonary:"))
x=a.keys()
y=a.values()
b=input("What would you like to sort:")
if  (b=="keys") :
  c=list(x)
else:
  c=list(y)
for i in range( len(c) ):
  for j in range ( 0, len(c)-i-1 ):
    if  ( c[j]   >  c[j+1] ):
      c[j], c[j+1]= c[j+1], c[j]
print("the sorted",b,"are:",c)
      
