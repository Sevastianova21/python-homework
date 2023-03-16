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


class Contact:
    def __init__(self, name: str, email: str, phone_number: str):
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def __str__(self):
        return f'Имя: {self.name}    Email: {self.email}    Номер телефона: {self.phone_number}\n'


class ContactBook:
    contacts = []

    def __init__(self):
        with open('phone.txt', 'r', encoding='UTF-8') as file:
            all_contacts = file.readlines()
            for i in range(len(all_contacts)):
                contact_str = all_contacts[i].split('   ')
                self.contacts.append(Contact((contact_str[0][5:]), (contact_str[1][8:]), contact_str[2][17:(-2)]))

    def save_contact(self):
        data = open('phone.txt', 'w', encoding='UTF-8')
        for i in range(len(self.contacts)):
            data.write(str(self.contacts[i]))
        data.close()

    def add_contact(self):
        self.contacts.append(Contact(input('Введите имя\n'), input('Введите Email\n'), input('Введите номер телефона\n')))

    def show_contact(self):
        data = open('phone.txt', 'r', encoding='UTF-8')
        i = 1
        for line in data:
            print(i, line)
            i = i + 1
        data.close()

    def rewrite_contact(self):
        string_number = int(input('Введите порядковый номер контакта, который хотите изменить\n'))
        match int(input('Изменить   1. Имя    2.Email     3. номер телефона\n')):
            case 1:
                self.contacts[string_number - 1].name = input('Новое имя \n')
            case 2:
                self.contacts[string_number - 1].email = input('Новый Email \n')
            case 3:
                self.contacts[string_number - 1].phone_number = input('Новый номер \n')

    def find_contact(self):
        find = input(' Введите имя, номер или Email \n')
        for i in range(len(self.contacts)):
            if self.contacts[i].name == find or self.contacts[i].email == find or self.contacts[i].phone_number == find:
                print(i + 1, self.contacts[i])

    def delete_contact(self):
        number = int(input('Введите номер строки контакта для удаления\n'))
        self.contacts.pop(number-1)


while what_to_do < 8:
    what_to_do = int(input('Введите номер соответствующего действия\n'))
    match what_to_do:
        case 1:
            contacts = ContactBook()
        case 2:
            contacts.save_contact()
        case 3:
            contacts.show_contact()
        case 4:
            contacts.add_contact()
        case 5:
            contacts.rewrite_contact()
        case 6:
            contacts.find_contact()
        case 7:
            contacts.delete_contact()
        case 8:
            print('завершение работы со справочником')