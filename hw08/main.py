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
def open_contact():
    with open('phone.txt', 'r') as file:
        contacts = file.readlines()
        print(contacts)
def save_contact():
    data = open('phone.txt', 'w')
    for i in range (len(contacts)):
        data.write(contacts[i])
    data.close()
def add_contact():
    with open('phone.txt', 'r') as file:
        contacts = file.readlines()
    contact = input('Введите контакт')
    contacts.append(contact)
    print('Контакт добавлен в справочник')
def show_contact():
    data = open('phone.txt', 'r')
    i = 1
    for line in data:
        print(i, line)
        i = i + 1
    data.close()
def rewrite_contact():
    with open('phone.txt', 'r') as file:
        contacts = file.readlines()
    string_number = int(input('Введите номер строки, которую хотите изменить'))
    new_contact = input('Введите новую информацию')
    contacts[string_number] = new_contact
def find_contact():
    with open('phone.txt', 'r') as file:
        contacts = file.readlines()
    find = input('Введите фамилию, имя или номер')
    for i in range(len(contacts)):
        contact = contacts.split()
        if find in contact:
            print(i, contacts[i])
def delete_contact():
    with open('phone.txt', 'r') as file:
        contacts = file.readlines()
    number = int(input('Введите номер строки контакта для удаления'))
    contacts = contacts.pop(number)
while what_to_do < 8:
    what_to_do = int(input('Введите номер соответствующего действия\n'))
    match what_to_do:
        case 1: open_contact()
        case 2: save_contact()
        case 3: show_contact()
        case 4: add_contact()
        case 5: rewrite_contact()
        case 6: find_contact()
        case 7: delete_contact()
        case 8: print('завершение работы со справочником')