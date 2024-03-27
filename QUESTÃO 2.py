
a = int(input("Digite um número para A: "))
b = int(input("Digite um número para B: "))
c = int(input("Digite um número para C: "))
equacaosegundo = b**2 -4*a*c
if equacaosegundo > 0:
    print("Existem duas raízes distintas.")
elif equacaosegundo == 0:
    print("Existem duas raízes iguais.")
else:
    print("Existem duas raízes imaginárias.")

