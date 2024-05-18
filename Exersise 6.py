string = 'Maria'
string_size = len(string)
if len(string) == 0: #'M'
    print(string*6)
elif len(string) == 2: #'Ma'
    print(string[1] + string[0])  #'Am'
elif len(string) == 3: #'Mar'
    print(string[2] + string[:2]) #'r'+ 'ma'
elif len(string) == 4: #Mari
    print(string[::-1]) #reverse 'Iram'
else:
    print('t'.join(string))    


    