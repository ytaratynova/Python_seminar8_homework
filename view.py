def input_class():
    class_number = input('Здравствуйте, введите класс? (7A/7B): ').upper()
    while class_number not in ['7a', '7A', '7b', '7B']:
        class_number = input('Внимательно введите класс в английской раскладке: ').lower()
    return class_number.upper()

def input_subject():
    what_subject = input('Открыть журнал по какому предмету (русский, математика, литература)? ').lower()
    while what_subject not in ['русский', 'математика', 'литература']:
        what_subject = input('Внимательно введите название предмета? ').lower()
    return what_subject

def class_menu():
    print()
    class_menu_list = ['Вывести журнал класса по предмету',
                       'Вывести успеваемость ученика',
                       'Закончить работу'
                      ]
    for i in range(len(class_menu_list)):
        print(f'    | {i+1}. {class_menu_list[i]}')
    print()

    user_input = int(input('Выберите действие из списка: '))
    while user_input not in [1, 2, 3]:
        user_input = int(input('Внимательно введите номер действия из списка: '))
    return user_input

def teacher_menu():
    print()
    teacher_menu = ['Вызвать к доске',
                    'Закончить урок и закрыть журнал'
                    ]
    for i in range(len(teacher_menu)):
        print(f'    | {i+1}. {teacher_menu[i]}')
    print()

    user_input = int(input('Выберите действие из списка: '))
    return user_input

def pupil_name():
    return input('Введите фамилию ученика: ')

def pupil_mark():
    return int(input(('Введите оценку за ответ: ')))

def subject_journal(cd, subject):
    print()
    print(f'Успеваемость по предмету {subject}:')
    print()
    print(f'       Ученик        успеваемость')
    print('_'*40)
    for key, values in cd.items():
        if subject == key:
           its_he = True
           journal = cd.get(key)
           for name, marks in journal.items():
               print(f'{name:20} {marks}')
    

               
def pupil_marks(cd, pupil):
    print('Успеваемость ученика, согласно Вашему запросу:')
    its_he = False
    for key, values in cd.items():
         journal = cd.get(key)
         for names, marks in journal.items():
            if pupil.lower() in names.lower():
                its_he = True
                print(f'{names:20} {key:15} {marks}')
    if not its_he:
        print(f'УЧЕНИК {pupil} НЕ НАЙДЕН!!!') 

def what_mark():
    mark = int(input('Оценка за ответ и работу на уроке: '))
    return mark
                
def exit_program():
    print('Завершение программы')      
    exit()
       
       
