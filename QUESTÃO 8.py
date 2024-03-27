idade = int(input("Para saber se você pode um eleitor(a), digite sua idade: "))
if idade <16:
    print("Você ainda não pode ser um eleitor(a)")
elif idade >=16 and idade <=18:
    print("Você pode ser um eleitor(a) facultativo.")
elif idade >=18 and idade <=65:
    print("Você já um eleitor(a) obrigatório.")
else:
    print("Seu voto não é mais obrigatório.")