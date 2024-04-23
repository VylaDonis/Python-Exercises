a = float(input('Enter the first number'))
b = float(input('Enter the seconde number'))
c = float(input('Enter the third number'))
d = float(input('Enter the forth number'))
if a > b and a > c and a > d:
    print('The first number is the largest')
elif b > a and b > c and b > d:
    print('The seconde number is the largest')
elif c > a and c > b and c > d:
    print('The third number is the largest')
else:
    print('The forth is the largest')            