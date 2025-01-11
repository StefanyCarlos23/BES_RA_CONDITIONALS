
a = int(input("Enter a number for A: "))
b = int(input("Enter a number for B: "))
c = int(input("Enter a number for C: "))
equacaosegundo = b**2 -4*a*c
if equacaosegundo > 0:
    print("Existem duas raízes distintas.")
elif equacaosegundo == 0:
    print("Existem duas raízes iguais.")
else:
    print("Existem duas raízes imaginárias.")

