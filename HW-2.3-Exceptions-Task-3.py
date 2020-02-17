
documents = [
   {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
   {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
   {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
   {"type": "insurance", "number": "10007"}
]

directories = {
       '1': ['2207 876234', '11-2', '5455 028765'],
       '2': ['10006', '5400 028765', '5455 002299'],
       '3': []
}

print('Добро пожаловать в "Помошник секретаря - 2020"!\n\n'
'Пожалуйста ознакомтесь с вариантами как я могу Вам помочь:\n'
'"p" - команда, которая попросит Вас ввести номер документа и выведет имя человека, которому он принадлежит\n'
'"l" – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"\n'
'"s" – команда, которая попросит Вас ввести номер документа и выведет номер полки, на которой он находится\n'
'"a" – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться\n'
'"b" – команда, которая выведет список имен всех владельцев документов.\n'
'"q" - выход из помошника\n')
commands = input('Вы готовы сделать свой выбор? Тогда введите нужную Вам команду: ')


def show_all(document):
    for document in documents:
        print(" ".join(document.values()))


def name_by_document_number(number_of_document):
    number_of_document = input('Введите номер документа: ')
    for entry_in_documents in documents:
        if entry_in_documents["number"] == number_of_document:
                return(entry_in_documents["name"])
    if entry_in_documents["number"] != number_of_document:
        return f'Документов с таким номером нет'


def get_number_shelf(number_of_document):
    number_of_document = input('Введите номер документа: ')
    for number_of_shelf, entry_in_documents in directories.items():
        if number_of_document in entry_in_documents:
            return f'Документы в шкафу №: {number_of_shelf}'
        else:
            return f'Документов с таким номером нет'


def add_new_data(new_document, new_shelf):
    new_document_number = input('Введите номер документа: ')
    new_document_type = input('Введите тип документа: ')
    new_document_name = input('Введите имя владельца документа: ')
    new_document_shelf = input('Введите номер полки на которой будет храниться документ: ')
    documents.append({"type": new_document_type, "number": new_document_number, "name": new_document_name})
    if new_document_shelf not in directories:
        directories[new_document_shelf] = [new_document_number]
    else:
        directories[new_document_shelf].append(new_document_number)
    return documents, directories


def show_all_names(documents):
    print(f'Имена всех владельцев всех документов: ')
    for name in documents:
        try:
            print(name["name"])
        except KeyError:
            print(f'Внимание: неверное внесение документа № "{name["number"]}" - не добавлены поля "name": "ФИО"')

for command in commands:
    if command == 'p':
        print(name_by_document_number(documents))
    elif command == 'l':
        show_all(documents)
    elif command == 's':
        print(get_number_shelf(directories))
    elif command == 'a':
        print(f'Информация успешно добавлена: {add_new_data(documents, directories)}', sep='\n')
    elif command == 'b':
        show_all_names(documents)
    else:
        print('До встречи.')
        break