userAge = int(input('Enter your age to find out if you can ride a Hopi Hari roller coaster: '))
userWeight = float(input('Now enter your weight: '))

if ((userAge >= 15) and (userWeight < 120)):
    print('Allowed!')
else:
    print('Prohibited!')