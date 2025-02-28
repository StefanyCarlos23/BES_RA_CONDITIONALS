userAge = int(input('To find out if you can be a voter, enter you age: '))

if userAge < 16:
    print('You cannot be a voter yet.')
elif 16 >= userAge <=18:
    print('You can be an optional voter.')
elif 18 <= userAge <= 65:
    print('You are required to be a voter.')
else:
    print('You are no longer required to vote')