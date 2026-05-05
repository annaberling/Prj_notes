import json

FILE_NAME = 'notes.json' # почему капсом?

# ======================
# ДАННЫЕ 
# ======================

def load_notes():
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except:
        return []
    
def save_notes(content):
    with open(FILE_NAME, 'w') as file:
        return json.dump(content, file, indent=4, ensure_ascii=False) # вот эту строчку я не понимаю\

# ======================
# ЛОГИКА
# ======================

def add_notes(text):
    content = load_notes()
    
    note = {
        'text': text,
        'done': False
    }
    
    content.append(note)
    save_notes(content)
    print('Запись добавлена')
    
def delete_note(index):
    content = load_notes()
    
    if not content:
        print('Нет записей')
        return
    
    if 0 <= index < len(content):
        content.pop(index)
        save_notes(content)
        print('Запись удалена')
    else:
        print('Такой записи нет')
    
def edit_note(index, text):
    content = load_notes()
    
    if not content:
        print('Нет записей')
        return
    
    if 0 <= index < len(content):
        content[index]['text'] = text 
        save_notes(content)
        print('Запись изменена')
    else:
        print('Такой записи нет')

def toggle_done(index):
    content = load_notes()
    
    if not content:
        print('Нет записей')
        return
    
    if 0 <= index < len(content): 
        content[index]['done'] = not content[index]['done']
        save_notes(content)
        print('Статус изменён')
    else:
        print('Такой записи нет')
        
def search_notes(query):
    content = load_notes()
    
    if not content:
        print('Нет записей')
        return
    
    found = False
    
    for i, note in enumerate(content, 1):
        if query in note['text'].lower():
            status = '✅' if not ['done'] else '❌'
            print(f'{i} - {note["text"]} [{status}]')
            found = True
            
    if not found:
        print('Ничего не найдено')

# ======================
# ВИД
# ======================

