ticket = input('Задайте шестизначный номер билета ')
if int(ticket[0])+int(ticket[1])+int(ticket[2]) == int(ticket[3])+int(ticket[4])+int(ticket[5]):
    print('О, да вы счастливчик!')
else:
    print('Не повезло')