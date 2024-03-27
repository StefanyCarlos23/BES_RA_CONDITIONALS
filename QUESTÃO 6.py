numero = int(input("Digite um número inteiro: "))
P = []
I = []
if numero %2 == 0:
    P.append(numero)
    print(f"O número {numero} é par.")
    return(P)
    
else:
    I.append(numero)
    print(f"O número {numero} é ímpar.")
    return(I)
print(f"Lista de números pares: {P}\n Lista de números ímpares: {I}")

