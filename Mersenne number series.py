#function to print mersenne number series for nth number

def   Mersenne(n):
  print("Mersenne numbers are:")
  for a in range(1,n):
    print(2**a-1)

c=int(input("Enter the mersenne number limit:"))
Mersenne(c)

