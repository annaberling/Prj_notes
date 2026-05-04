
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
def print_notes(content, show_status=True):
    for i, note in enumerate(content, 1):
        if show_status:
            status = '✅' if note['done'] else '❌'
            print(f'{i} - {note['text']} [{status}]')
        else:
            print(f'{i} - {note['text']}')

# Проверка контента внутри + загрузка        
def get_notes():
    content = load_notes()
    if not content:
        print('Нет записей')
        return None
    return content
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
         
# Изменение статуса
def toggle_done():
    content = load_notes()
    
    if not content:
        print('Нет записей')
        return
    print_notes(content)
    
    try:
        note = int(input('Какую запись отметить?'))
    except:
        print('Введите число')
        return
    
    index = note - 1
    
    if 0 <= index < len(content):
        current = content[index]['done']
        content[index]['done'] = not current
        
        save_notes(content)
        
        print('Статус изменён')
        
    else:
        print('Такой записи нет')
        
# Фильтры записей
def show_filtered():
    content = load_notes()
    
    if not content:
        print('Нет записей')
        return
    
    mode = input('1 - все, 2 - ✅, 3 - ❌:')
    
    for note in content:
        if mode == '1':
            print(note['text'])
        elif mode == '2' and note['done']:
            print(note['text'])
        elif mode == '3' and not note ['done']:
            print(note['text'])
            
# Показать меню
def menu():
    actions = {
        '1': add_note,
        '2': show_notes,
        '3': count_notes,
        '4': delete_note,
        '5': edit_note,
        '6': search_note,
        '7': toggle_done
    }
    
    while True:
        print('\n1 - Добавить запись')
        print('2 - Посмотреть записи')
        print('3 - Количество записей')
        print('4 - Удалить запись')
        print('5 - Изменить запись')
        print('6 - Поиск записи')
        print('7 - Изменить статус')
        print('0 - Выход')
        
        command = input('Выбери ').strip()
        
        if command == '0':
            break
        
        action = actions.get(command)
        if action:
            action()
        else:
            print('Нет такой команды')
    
menu()


    
