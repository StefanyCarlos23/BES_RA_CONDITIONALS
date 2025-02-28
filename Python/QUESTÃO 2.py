
a = int(input("Enter a number for A: "))
b = int(input("Enter a number for B: "))
c = int(input("Enter a number for C: "))
quadraticEquation = b**2 -4*a*c
if quadraticEquation > 0:
    print("There are two distinct roots.")
elif quadraticEquation == 0:
    print("There are two equal roots.")
else:
    print("There are two imaginary roots.")