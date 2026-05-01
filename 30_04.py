
import json

# Открыть заметку
def load_notes():
    try:
        with open('notes.json', 'r') as file:
            return json.load(file)
    except:
        return []
        
# Сохранить заметку с новым текстом
def save_notes(content):
    with open('notes.json', 'w') as file:
        json.dump(content, file, indent=4, ensure_ascii=False)    

# Вывод заметки         
def print_notes(content):
    for i, note in enumerate(content, 1):
        status = '✅' if note['done'] else '❌'
        print(f'{i} - {note["text"]} [{status}]')
#--------------------------------------------------
# Добавить новую заметку в файл
def add_note():
    content = load_notes()
    
    text = input('Что записать? ').strip()
    
    note = {
        'text': text,
        'done': False
    }
    
    content.append(note)
    
    save_notes(content)

# Показать заметки в файле
def show_notes():
    content = load_notes()
    if not content:      # if content == []:
        print('Нет записей')
        return
    print('Мои записи: ')
    print_notes(content)

# Показать количество записей
def count_notes():
    content = load_notes()
    if not content:
        print('Нет записей')
    else:
        print(f'Всего записей: {len(content)}')

# Удалить запись
def delete_note():
    content = load_notes()
        
    if not content:
        print('Нет записей')
        return 
        
    print_notes(content)
            
    try:
        note = int(input('Какую запись удалить? '))
    except:
        print('Введите число')
        return
        
    index = note - 1 
        
    if 0 <= index < len(content):
        content.pop(index)
            
        save_notes(content)
    
        print('Запись удалена')
            
    else:
        print('Нет такой записи')

# Изменить запись
def edit_note():
        content = load_notes()
        
        if not content:
            print('Нет записей')
            return
        print_notes(content)
        try:
            note = int(input('Какую запись изменить? '))
        except:
            print('Введите число')
            return
                
        index = note - 1 
            
        if 0 <= index < len(content):
            note = input('Введи новый текст: ')
            content[index]["text"] = note.strip()
            
            save_notes(content)

            print('Запись изменена')
        else:
            print('Такой записи нет')

# Поиск в заметках            
def search_note(): 
    content = load_notes()
    
    if not content:
        print('Нет записей')
        return
    
    query = input('Что ищем? ').strip().lower()
    
    found = False
    
    for i, note in enumerate(content, 1):
        if query in note["text"].lower():
            status = '✅' if note['done'] else '❌'
            print(f'{i} - {note["text"]} [{status}]')
            found = True
            
    if not found:
        print('Ничего не найдено')
            
# Показать меню
def menu():
    while True:
        print('\n1 - Добавить запись')
        print('2 - Посмотреть записи')
        print('3 - Количество записей')
        print('4 - Удалить запись')
        print('5 - Изменить запись')
        print('6 - Поиск записи')
        print('0 - Выход')
        
        command = input('Выбери: ').strip()
        if command == '1':
            add_note()
        elif command == '2':
            show_notes()
        elif command == '3':
            count_notes()
        elif command == '4':
            delete_note()
        elif command == '5':
            edit_note()
        elif command == '6':
            search_note()
        elif command == '0':
            break


menu()


    
