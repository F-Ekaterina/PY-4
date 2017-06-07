students_list = [
         {'имя' : 'Сергей Иванов' , 'gender' : 'муж', 'experience' : True , 'homeworks' : [10 , 10 , 9 , 5 ,9 ], 'exam' : 10 },
         {'имя' : 'Никита Петров' , 'gender' : 'муж', 'experience' : False , 'homeworks' : [7 , 6 , 8 , 10 , 10 ], 'exam' : 9},
         {'имя' : 'Михаил Дягилев' , 'gender' : 'муж', 'experience' : True , 'homeworks' : [6 , 5 , 10 , 8 , 9 ], 'exam' :8},
         {'имя' : 'Вячеслав Марков' , 'gender' : 'муж', 'experience' : True , 'homeworks' : [10 , 10 , 9 , 5 ,9 ], 'exam' : 10},
         {'имя' : 'Сергей Клименок' , 'gender' : 'муж', 'experience' : False , 'homeworks' : [7 , 8 , 8 , 8 , 10 ], 'exam' : 8},
         {'имя' : 'Олеся Шеметова' , 'gender' : 'жен', 'experience' : True , 'homeworks' : [6 , 8 , 7 , 4 , 5 ], 'exam' : 5},
         {'имя' : 'Ольга Кайзер' , 'gender' : 'жен', 'experience' : False , 'homeworks' :[5 , 8 , 7 , 10 , 10 ], 'exam' : 8},
         {'имя' : 'Евгения Васильева' , 'gender' : 'жен', 'experience' : True , 'homeworks': [8 , 10 , 8 , 7 , 6 ], 'exam' : 7},
         {'имя' : 'Александр Серга' , 'gender' : 'муж', 'experience' : False , 'homeworks' :[6 , 8 , 7 , 4 , 5 ], 'exam' : 5},
         {'имя' : 'Екатерина Федорова' , 'gender' : 'жен', 'experience' : True , 'homeworks' : [9 , 9 , 8 , 7 ,6 ], 'exam' : 8}
      ]

students=['Сергей Иванов', 'Никита Петров', 'Михаил Дягилев', 'Вячеслав Марков',\
          'Сергей Клименок', 'Олеся Шеметова', 'Ольга Кайзер', 'Евгения Васильева', \
          'Александр Серга', 'Екатерина Федорова']

quantity_students = len(students)
quantity_homeworks = 5

print('_____________________________________', '\n')


def middle_rating_group():
    homework_ratings = []
    exam_rating = []
    for student in students_list:
        homework_ratings.append(sum(student['homeworks']))
        middle_rating_homeworks = sum(homework_ratings) / (quantity_homeworks * quantity_students)
        exam_rating.append(student['exam'])
        middle_rating_exam = sum(exam_rating) / quantity_students
    print('средняя оценка за домашние задания по группе:', 'X=', middle_rating_homeworks)
    print('средняя оценка за экзамен по группе:', 'Y=', middle_rating_exam)
    return


def middle_ball_gender():
    rating_man = []
    rating_woman = []
    exam_man = []
    exam_woman = []
    for student in students_list:
        if student['gender'] == 'муж':
            rating_man.extend(student['homeworks'])
            exam_man.append(student['exam'])
        else:
            rating_woman.extend(student['homeworks'])
            exam_woman.append(student['exam'])

    middle_rating_man = sum(rating_man) / len(rating_man)
    middle_rating_woman = sum(rating_woman) / len(rating_woman)
    middle_exam_man = sum(exam_man) / len(exam_man)
    middle_exam_woman = sum(exam_woman) / len(exam_woman)
    print('средняя оценка за дз , мужчины: A=', round(middle_rating_man, 2))
    print('средняя оценка за дз, женщины: C=', middle_rating_woman)
    print('средняя оценка за экзамен, мужчины: B=', round(middle_exam_man, 2))
    print('cpедняя оценка за экзамен, женщины: D=', middle_exam_woman)
    return


def middle_ball_experience():
    rating_experience = []
    rating_not_expirience = []
    exam_experience = []
    exam_not_experience = []
    for student in students_list:
        if student['experience'] == True:
            rating_experience.extend(student['homeworks'])
            exam_experience.append(student['exam'])
        else:
            rating_not_expirience.extend(student['homeworks'])
            exam_not_experience.append(student['exam'])

    middle_rating_experience = sum(rating_experience) / len(rating_experience)
    middle_rating_not_experience = sum(rating_not_expirience) / len(rating_not_expirience)
    middle_exam_experience = sum(exam_experience) / len(exam_experience)
    middle_exam_not_experience = sum(exam_not_experience) / len(exam_not_experience)
    print('средняя оценка за дз , студенты с опытом: E=', round(middle_rating_experience))
    print('средняя оценка за дз, студенты без опыта: G=', middle_rating_not_experience)
    print('средняя оценка за экзамен, студенты с опытом: F=', round(middle_exam_experience, 2))
    print('cpедняя оценка за экзамен, студенты без опыта: H=', middle_exam_not_experience)
    return


def min_max_rating():
    score_table = []
    name_table = []
    for student in students_list:
        rating_student=(0.6*(sum(student['homeworks'])/len(student['homeworks']))+ 0.4*(student['exam']))
        score_table.append(rating_student)
        name_table.append(student['имя'])
    #print(score_table)
    #print(name_table)
    for name, rating in zip(name_table, score_table):
        min_rating=min(score_table)
        max_rating=max(score_table)
        if rating== min_rating:
            print('Худший студент', name, 'с интегральной оценкой Z=', min_rating)
        elif rating== max_rating:
            print('Лучший студент', name, 'c интегральной оценкой Z=', max_rating)

def main():
    while True:
        user_input = input('''Введите команду, которую хотите выполнить:
  XY- среднюю оценку за домашние задания и за экзамен по всем группе
  ABCD- средняя оценка за домашние работы и за экзамен в зависимости от пола
  EFGH- средняя оценка за домашние работы и за экэкзамен в зависимости от наличия опыта
  Z- лучшие/ худшие студенты''')
        if user_input == 'XY':
            middle_rating_group()
            print('________________', '\n')
        elif user_input == 'ABCD':
            middle_ball_gender()
            print('________________', '\n')
        elif user_input == 'EFGH':
            middle_ball_experience()
            print('________________', '\n')
        elif user_input == 'Z':
            min_max_rating()
            print('________________','\n')

main()
