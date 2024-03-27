idade = int(input("Para descobrir se você já pode se aposentar. Digite sua idade: "))
tempotrab = int(input("Agora digite quantos anos de serviço você tem: "))
if(idade >=65):
    print("Você já pode se aposentar!!")
elif(tempotrab >=30):
    print("Você já pode se aposentar!!")
elif((idade >=60) and (tempotrab >=25)):
    print("Você já pode se aposentar!!")
else:
    print("Você ainda não pode se aponsetar.")