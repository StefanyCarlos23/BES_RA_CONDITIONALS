while True:
    firstGrade = float(input('Enter your first term grade (0 to 10): '))
    if firstGrade <= 0 or firstGrade >= 10:
        print("The first grade must to be between 0 and 10. Please enter them again.")
        continue

    while True:
        secondGrade = float(input('Now, enter you second term grade (0 to 10): '))  
        if secondGrade <= 0 or secondGrade >= 10:
            print("The second grade must to be between 0 and 10. Please enter them again.")
            continue
        else:
            average = (firstGrade + secondGrade) / 2
            while True:
                print('-'*50)
                print(f'The average of the grades is {average:.2f}')
                print('-'*50)

                university = int(input(f'Enter the code of your university\n'
                                '1 - PUCPR\n'
                                '2 - UNICAMP\n'
                                '3 - EXIT\n'
                                'Your choice: '
                                ))
                
                if university == 3:
                    print("Exiting the program. Goodbye!")
                    break
                elif university < 1 or university > 3:
                    print('University code invalid, enter again:')
                    continue

                if university == 1:
                    if average >= 7.0:
                        print('-'*50)
                        print('You are approved!!')
                    elif 6.9 <= average >= 4.0:
                        print('-'*50)
                        print('You are in recovery')
                    else:
                        print('-'*50)
                        print('You are failed')
                elif university == 2:
                    if average >= 5.0:
                        print('-'*50)
                        print('You are approved!!')
                    else:
                        print('-'*50)
                        print('In final exam')