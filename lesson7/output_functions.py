from tinydb.table import Document


def output_contacts(contacts: list[Document]):
    for contact in contacts:
        output_contact(contact)


def output_contact(contact: Document):
    print(f'id: {contact.doc_id}')
    print(f'Фамилия: {contact["lastname"]}')
    print(f'Имя: {contact["firstname"]}')
    print(f'Телефон: {contact["phone"]} ({contact["description"]})')
    print('')
