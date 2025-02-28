userAge  = int(input('To find out if you can retire, enter your age: '))
jobTime = int(input('Now, enter how many years of service you have: '))

if userAge >= 65:
    print('Congratulations, you can retire!!')
elif jobTime >= 30:
    print('Congratulations, You can retire!!')
elif userAge >=60 and jobTime >= 25:
    print('Congratulations, You can retire!!.')
else:
    print('You cannot retire yet.')
