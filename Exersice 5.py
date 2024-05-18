income = float(input('Enter your income: '))
presentages = [ 24, 31, 34] 
if income < 6700:
    presentage = 24
    tax = (income/100) * 24
    tax_income = income - tax
    print('Your income after taxes is', tax_income, 'euros')
elif 6700 < income < 9700:
    presentage = 31
    tax = (income/100) * 31
    tax_income = income - tax
    print('Your income after taxes is', tax_income, 'euros') 
else:
    presentage = 34
    tax = (income/100) * 34
    tax_income = income - tax
    print('Your income after taxes is', tax_income, 'euros')    


