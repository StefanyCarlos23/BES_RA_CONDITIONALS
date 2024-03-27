nome = input("Olá, nesse programa você irá descobrir qual seu peso ideal.\n Para começar, digite o seu nome: ")
altura = float(input("Digite a sua altura em metros: "))
sexo = input("Digite o seu sexo (Masculino ou Feminino): ")
if sexo == "Masculino":
    pesoideal = 72.7*altura- 58
    print(f"{nome} seu peso ideal é {pesoideal}kg.")
elif sexo == "Feminino":
    pesoIdeal = 62.1*altura-44.7
    print(f"{nome} seu peso ideal é {pesoIdeal}kg.")
else:
    print("Sexo inválido")