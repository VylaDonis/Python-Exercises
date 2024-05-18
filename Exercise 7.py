answer_one = int(input('What is 2*2?'))
if answer_one == 4:
    print('This is correct')
else:
    print('You failed') 
answer_two = int(input('What is 6/3?'))
if answer_two == 2:
    print('This is correct') 
else:
    print('Wrong') 
answer_three = int(input('What is 9*9?'))
if answer_three == 81:
    print('Correct')
else:
    print('You failed the test') 
if answer_one == 4 and answer_two == 2 and answer_three == 81:
    print('Congradulations. You passed the test')
else:
    print('You faile the test. Try again.')        

