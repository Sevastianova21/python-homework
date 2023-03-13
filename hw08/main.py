print('Меню работы с телефонным справочником\n'
'1. Открыть файл\n'
'2. Сохранить файл\n'
'3. Показать контакты\n'
'4. Добавить контакт\n'
'5. Изменить контакт\n'
'6. Найти контакт\n'
'7. Удалить контакт\n'
'8. Выход')
what_to_do = 0
contacts = []
def open_contact():
    with open('phone.txt', 'r') as file:
        contacts = file.readlines()
        return contacts
def save_contact(contacts):
    data = open('phone.txt', 'w')
    for i in range (len(contacts)):
        data.write(contacts[i])
    data.close()
def add_contact(contacts):
    contacts.append(input('Введите контакт '))
    print('Контакт добавлен в справочник ')
    return contacts
def show_contact():
    data = open('phone.txt', 'r')
    i = 1
    for line in data:
        print(i, line)
        i = i + 1
    data.close()
def rewrite_contact(contacts):
    string_number = int(input('Введите номер строки, которую хотите изменить '))
    contacts[string_number-1] = input('Введите новую информацию ') + '\n'
    return contacts
def find_contact(contacts):
    find = input('Введите фамилию, имя или номер \n')
    for i in range(len(contacts)):
        contact = contacts[i].split()
        if find in contact:
            print(i, contacts[i])

def delete_contact(contacts):
    number = int(input('Введите номер строки контакта для удаления'))
    contacts = contacts.pop(number)
    return contacts

while what_to_do < 8:
    what_to_do = int(input('Введите номер соответствующего действия\n'))
    match what_to_do:
        case 1: contacts = open_contact()
        case 2: save_contact(contacts)
        case 3: show_contact()
        case 4: contacts = add_contact(contacts)
        case 5: contacts = rewrite_contact(contacts)
        case 6: find_contact(contacts)
        case 7: contacts = delete_contact(contacts)
        case 8: print('завершение работы со справочником')