from tinydb import TinyDB, Query
from tinydb.table import Document
from pathlib import Path
from file_functions import export_to_txt, export_to_csv, import_from_txt, import_from_csv
from input_functions import input_menu_selection, input_text, input_text_default, select_contact
from output_functions import output_contacts

db = TinyDB('db.json')
contactsTable = db.table('contacts')
settingsTable = db.table('settings')


def search_contains(value: str, search: str):
    return search.lower() in value.lower()


def get_next_id():
    global settingsTable

    q = Query()
    results = settingsTable.get(q.name == 'last_id')

    if results is None:
        settingsTable.insert({
            'name': 'last_id',
            'value': 1
        })
        return 1

    last_id = results[0]
    last_id['value'] += 1

    settingsTable.update(last_id, q.name == 'last_id')

    return last_id['value']


def main_menu():
    print('1: Просмотр контактов')
    print('2: Добавить контакт')
    print('3: Поиск контактов')
    print('4: Импорт контактов')
    print('5: Экспорт контактов')
    print('0: Выход')
    print('')

    user_selection = input_menu_selection(['1', '2', '3', '4', '5', '0'])

    if user_selection == '1':
        show_contacts()
    elif user_selection == '2':
        add_contact()
    elif user_selection == '3':
        search_contacts()
    elif user_selection == '4':
        import_contacts()
    elif user_selection == '5':
        export_contacts()


def show_contacts():
    global contactsTable

    contacts = contactsTable.all()

    if len(contacts) == 0:
        print('Список контактов пуст')
        print('')
        main_menu()
    else:
        output_contacts(contacts)
        contacts_actions(contacts)


def add_contact():
    global contactsTable

    lastname = input_text('Фамилия')
    firstname = input_text('Имя')
    phone = input_text('Телефон')
    description = input_text('Описание')

    contactsTable.insert({
        'lastname': lastname,
        'firstname': firstname,
        'phone': phone,
        'description': description
    })

    print('Контакт добавлен')
    print('')
    main_menu()


def edit_contact(contact: Document):
    global contactsTable

    print(f'Редактирование контакта {contact.doc_id}')
    print('Оставьте поле пустым чтобы сохранить текущее значение')

    contact['lastname'] = input_text_default('Фамилия', contact['lastname'])
    contact['firstname'] = input_text_default('Имя', contact['firstname'])
    contact['phone'] = input_text_default('Телефон', contact['phone'])
    contact['description'] = input_text_default('Описание', contact['description'])

    contactsTable.upsert(contact)

    print('Изменения сохранены')
    print('')
    main_menu()


def search_contacts():
    global contactsTable

    search_query = input_text('Введите запрос')

    q = Query()
    contacts = contactsTable.search(
        q.firstname.test(search_contains, search_query)
        | q.lastname.test(search_contains, search_query)
        | q.phone.test(search_contains, search_query)
    )

    if len(contacts) == 0:
        print('Не найдены контакты соответсвующие запросу')
        print('')
        main_menu()
    else:
        output_contacts(contacts)
        contacts_actions(contacts)


def import_contacts():
    global contactsTable

    print('1: Импорт из txt')
    print('2: Импорт из csv')
    print('0: Выход в меню')
    print('')

    user_selection = input_menu_selection(['1', '2', '0'])

    if user_selection == '0':
        main_menu()
        return

    file_name = input_text('Введите название файла')

    file = Path(file_name)
    if not file.is_file():
        print('Файл не найден')
        print('')
        main_menu()
        return

    if user_selection == '1':
        contacts = import_from_txt(file_name)
    else:
        contacts = import_from_csv(file_name)

    if len(contacts) > 0:
        contactsTable.insert_multiple(contacts)

    print(f'Импортированно контактов: {len(contacts)}')
    print('')
    main_menu()


def export_contacts():
    global contactsTable

    print('1: Экспорт в txt')
    print('2: Экспорт в csv')
    print('0: Выход в меню')
    print('')

    user_selection = input_menu_selection(['1', '2', '0'])

    if user_selection == '0':
        main_menu()
        return

    file_name = input_text('Введите название файла')

    contacts = contactsTable.all()

    if user_selection == '1':
        export_to_txt(contacts, file_name)
    else:
        export_to_csv(contacts, file_name)

    print('Контакты экспортированы')
    print('')
    main_menu()


def contacts_actions(contacts: list[Document]):
    print('1: Редактировать')
    print('2: Удалить')
    print('0: Выход в меню')
    print('')

    user_action = input_menu_selection(['1', '2', '0'])

    if user_action == '0':
        main_menu()
        return

    contact = select_contact(contacts)

    if user_action == '1':
        edit_contact(contact)
    else:
        delete_contact(contact)


def delete_contact(contact: Document):
    global contactsTable

    contactsTable.remove(doc_ids=[contact.doc_id])

    print('Контакт удален')
    print('')
    main_menu()


main_menu()
