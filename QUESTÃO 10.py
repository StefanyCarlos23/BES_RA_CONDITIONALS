notaB1 = float(input("Digite sua nota no primero bimestre: "))
notaB2 = float(input("Digite sua nota no segundo bimestre: "))
media = notaB1 + notaB2/2
(input(f"Sua nota média é {media}"))
uni = int(input("Digite o códico da sua universidade\n 1 - PUCPR\n 2 - UNICAMP\n"))
if uni == 1:
    if (media>=7.0):
        print("Aprovado!.")
    elif (media >=4 and media <7):
        print("Em exame final.")
    else:
        print("Reprovado!")
if uni == 2:
    if media >=5.0:
        print("Aprovado!")
    else:
        print("Em exame.")