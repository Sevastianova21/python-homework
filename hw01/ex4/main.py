m = input('размер шоколадки в дольках по вертикали ')
n = input('размер шоколадки в дольках по горизонтали ')
k = input ('Сколько хотим отломить долек ')
if int(m) * int(n) < int(k):
    print('не надо жадничать, это больше, чем вся шоколадка')
elif int(k)%int(m)==0 or int(k)%int(n)==0:
    print ('можно отломить одним разломом')
else:
    print('нельзя отломить одним разломом')
