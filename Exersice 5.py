
income = float(input('Enter your income: '))# could not conver a string to float 
presentage = [ 24, 31, 34] 
tax = (income/100) * presentage
tax_income = income - tax
if income < 6700:
    presentage = 24
    print('Your income after taxes is', tax_income, 'euros')
elif 6700 < income < 9700:
    presentage = 31
   print('Your income after taxes is', tax_income, 'euros') 
else:
presentage = 34
print('Your income after taxes is', tax_income, 'euros')
# I couldn't fix the error , so don't know id is correct
