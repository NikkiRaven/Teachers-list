import random

students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()
classes = ['Математика', 'Русский язык', 'Информатика']
students_marks = {}
for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1, 5) for i in range(3)]
        students_marks[student][class_] = marks
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Изменить данные
        3. Вывести средний балл по определенному ученику
        4. Вывести средний балл по всем предметам по каждому ученику
        5. Вывести оценки по определенногму ученику
        6. Вывести все оценки по всем ученикам
        7. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
            break
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')

    elif command == 2:
        print('''
                Вид изменений:
                1. Удалить данные
                2. Корректировать данные
                ''')

        postcommand = int(input('Вид изменений:'))
        if postcommand == 1:
            print('1. Удалить данные')
            print('''
                    Категории:
                    1. Оценки
                    2. Предметы
                    3. Ученики
                    ''')

            lastcommand = int(input('Категории:'))
            if lastcommand == 1:
                while True:
                    print('1. Оценки')
                    student = input('Введите имя ученика: ')
                    if student not in students:
                        print('ОШИБКА: неверное имя ученика')
                    else:
                        while True:
                            class_ = input('Введите предмет: ')
                            if class_ not in classes:
                                print('ОШИБКА: неверно указан предмет')
                            else:
                                print(students_marks[student][class_])
                                mark_number = int(input('Введите оценку, подлежащую удалению: '))
                                if mark_number in students_marks[student][class_]:
                                    students_marks[student][class_].remove(mark_number)
                                    print('Оценка успешно удалена')
                                    print(students_marks[student][class_])
                                    break
                                else:
                                    print('Оценка в журнале отсутствует')

            elif lastcommand == 2:
                while True:
                    print('2. Предметы')
                    student = input('Введите имя ученика: ')
                    if student not in students:
                        print('ОШИБКА: неверное имя ученика')
                    else:
                        while True:
                            class_ = input('Введите предмет: ')
                            if class_ not in classes:
                                print('ОШИБКА: неверно указан предмет')
                            else:
                                del students_marks[student][class_]
                                print('Предмет успешно удален')
                                print(f'''{student}
                                    {students_marks[student]}''')
                                break

            else:
                print('3.Ученики')
                while True:
                    student = input('Введите имя ученика: ')
                    if student not in students:
                        print('ОШИБКА: неверное имя ученика')
                    else:
                        del students_marks[student]
                        print(f'''{student}
                            {students_marks}''')
                        break

        else:
            print('2. Корректировать данные')
            print('''
                            Категории:
                            1. Оценки
                            2. Предметы
                            3. Ученики
                            ''')
            lastcommand = int(input('Категории:'))
            if lastcommand == 1:
                while True:
                    print('1. Оценки')
                    student = input('Введите имя ученика: ')
                    if student not in students:
                        print('ОШИБКА: неверное имя ученика')
                    else:
                        while True:
                            class_ = input('Введите предмет: ')
                            if class_ not in classes:
                                print('ОШИБКА: неверно указан предмет')
                            else:
                                print(students_marks[student][class_])
                                mark_number = int(input('Введите оценку, подлежащую изменению: '))
                                new_mark_number = int(input('Введите новую оценку: '))
                                if mark_number in students_marks[student][class_]:
                                    students_marks[student][class_].remove(mark_number)
                                    students_marks[student][class_].append(new_mark_number)
                                    print('Оценка успешно заменена')
                                    print(students_marks[student][class_])
                                    break
                                else:
                                    print('Оценка в журнале отсутствует')

            elif lastcommand == 2:
                while True:
                    print('2. Предметы')
                    student = input('Введите имя ученика: ')
                    if student not in students:
                        print('ОШИБКА: неверное имя ученика')
                    else:
                        while True:
                            subject = input('Введите предмет, подлежащий изменению:')
                            if subject not in students_marks[student].keys():
                                print('ОШИБКА: неверно указан предмет или предмет отсутствует')
                            else:
                                new_subject = input('Введите новый предмет:')
                                if new_subject in students_marks[student].keys():
                                    print('ОШИБКА: ученик уже записан на данный предмет')
                                else:
                                    students_marks[student][new_subject] = students_marks[student][subject]
                                    del students_marks[student][subject]
                                    print('Предмет успешно заменен')
                                    print(f'''{student}
                                        {students_marks[student]}''')
                                    break

            elif lastcommand == 3:
                while True:
                    print('3. Ученики')
                    student = input('Введите имя ученика: ')
                    if student not in students:
                        print('ОШИБКА: неверное имя ученика')
                    else:
                        new_student = input('Введите измененное имя ученика: ')
                        if new_student in students_marks.keys():
                            print('ОШИБКА: имя ученика не изменилось')
                        else:
                            students_marks[new_student] = students_marks[student]
                            del students_marks[student]
                            print('Имя ученика успешно заменено')
                            print(f'''{new_student}
                                {students_marks[new_student]}''')
                            break

    elif command == 3:
        while True:
            print('3. Вывести средний балл по определенному ученику')
            student = input('Введите имя ученика: ')
            if student not in students:
                print('ОШИБКА: Ученик отсутствует')
            else:
                subject = input('Введите предмет: ')
                if subject not in students_marks[student].keys():
                    print('ОШИБКА: Предмет отсутствует или введен неверно')
                else:
                    marks_sum = sum(students_marks[student][subject])
                    marks_count = len(students_marks[student][subject])
                    print(f'''{student}
                        {students_marks[student]}''')
                    print(f'{subject} - {marks_sum // marks_count}')
                    print()
                    break

    elif command == 4:
        print('4. Вывести средний балл по всем предметам по каждому ученику')
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum // marks_count}')
            print()
            break

    elif command == 5:
        while True:
            print('5. Вывести оценки по определенногму ученику')
            student = input('Введите имя ученика: ')
            if student not in students:
                print('ОШИБКА: Ученик отсутствует')
            else:
                for class_ in classes:
                    print(f'\t{class_} - {students_marks[student][class_]}')
                print()
                break

    elif command == 6:
        print('6. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
            break

    elif command == 7:
        print('7. Выход из программы')
        break
