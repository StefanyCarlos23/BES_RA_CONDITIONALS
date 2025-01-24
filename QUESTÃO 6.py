E = []
O = []

while True:
    number = int(input("Enter a integer (or type to '000'): "))
    if number == 000:
        break
    elif number %2 == 0:
        O.append(number)
        print(f"The number {number} is odd.")
    elif number %2 != 0:
        E.append(number)
        print(f"The number {number} is even.")
    else:
        print(f"Invalid input")
print(f"Even numbers list: {E}\n Odd numbers list: {O}")
