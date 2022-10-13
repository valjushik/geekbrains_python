from tinydb.table import Document


def export_to_txt(contacts: list[Document], file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for contact in contacts:
            f.write(f'{contact["lastname"]}\n')
            f.write(f'{contact["firstname"]}\n')
            f.write(f'{contact["phone"]}\n')
            f.write(f'{contact["description"]}\n')
            f.write('\n')


def export_to_csv(contacts: list[Document], file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for contact in contacts:
            f.write(f'{contact["lastname"]},{contact["firstname"]},{contact["phone"]},{contact["description"]}\n')


def import_from_txt(file_name):
    contacts = []

    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()

        contact_lines = []
        while True:
            line = lines.pop(0).strip() if len(lines) > 0 else ''
            if line != '':
                contact_lines.append(line)
                continue

            if len(contact_lines) != 4:
                print("Ошибка в файле")
                return []

            contacts.append({
                'lastname': contact_lines[0].strip(),
                'firstname': contact_lines[1].strip(),
                'phone': contact_lines[2].strip(),
                'description': contact_lines[3].strip()
            })
            contact_lines = []

            if len(lines) == 0:
                break

    return contacts


def import_from_csv(file_name):
    contacts = []
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()

        for line in lines:
            contact_lines = line.split(',')

            if len(contact_lines) != 4:
                print("Ошибка в файле")
                return []

            contacts.append({
                'lastname': contact_lines[0].strip(),
                'firstname': contact_lines[1].strip(),
                'phone': contact_lines[2].strip(),
                'description': contact_lines[3].strip()
            })

    return contacts
