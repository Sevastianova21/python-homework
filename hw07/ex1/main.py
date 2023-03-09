# про винни пуха
def ryphm(string):
    list_let = list()
    letters = []
    list_1 = ['у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю']
    phrases = string.split()
    for i in range(len(phrases)):
        letters = phrases[i]
        list_let.append(0)
        for j in range(len(letters)):
            if letters[j] in list_1:
                list_let[i] = list_let[i] + 1
    if len(set(list_let)) == 1:
        return 'Парам пам-пам'
    else:
        return 'пам парам'
string = input('Введи стишок, Винни ')
print(ryphm(string))