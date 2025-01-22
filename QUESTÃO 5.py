userName = input("Hello! In this program you will discover what is your ideal weight.\n To start, please enter your name: ")
userHeight = float(input("Now, enter your height in meters:"))
userGender = input("Finally, enter your biological sex (Male or Female")

if userGender == "Male":
    idealWeight = 72.7*userHeight- 58
    print(f"{userName} your ideal weight is {idealWeight:.2f} kilograms.")
elif userGender == "Female":
    idealWeight = 62.1*userHeight-44.7
    print(f"{userName} your ideal weight is {idealWeight:.2f} kilograms.")
else:
    print("Invalid input for biological sex.")