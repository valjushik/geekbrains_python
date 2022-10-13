from tinydb.table import Document


def input_menu_selection(variants):
    while True:
        user_input = input('Выберите пункт: ')
        if user_input in variants:
            return user_input
        print('Некорректный вариант')


def input_text(prompt):
    while True:
        user_input = input(f'{prompt}: ').strip()
        if user_input != '':
            return user_input
        print('Нельзя вводить пустое значение')


def input_text_default(prompt, default_value):
    while True:
        user_input = input(f'{prompt}[{default_value}]: ').strip()
        if user_input != '':
            return user_input

        return default_value


def select_contact(contacts: list[Document]):
    while True:
        user_input = input('Введите id контакта: ')
        if not user_input.isdigit():
            print('Необходимо ввести корректное число')
            continue

        user_input = int(user_input)

        found_contacts = list(filter(lambda x: x.doc_id == user_input, contacts))

        if len(found_contacts) == 0:
            print('Необходимо ввести существующее значение')
            continue

        return found_contacts[0]
