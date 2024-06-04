
import random

students = ['Андрей', 'Анна', 'Артём', 'Антонина', 'Богдан', 'Владимир', 'Вероника', 'Геннадий', 'Дмитрий', 'Евгений',
            'Елена', 'Игорь', 'Ирина', 'Кирилл', 'Константин', 'Лев', 'Максим', 'Мария', 'Михаил', 'Наталья', 'Никита',
            'Олег', 'Ольга', ]

selected_students = random.sample(students, 5)
print("имена студентов, которые будут отвечать на уроке:")

for student in selected_students:
    print(student)

for student in selected_students:
    students.remove(student)
