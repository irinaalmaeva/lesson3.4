
import random

students = ['Алексей', 'Анна', 'Артём', 'Антонина', 'Борис', 'Владимир', 'Вероника', 'Григорий', 'Дмитрий', 'Евгений',
            'Елена', 'Игорь', 'Ирина', 'Кирилл', 'Константин', 'Лев', 'Максим', 'Мария', 'Михаил', 'Наталья', 'Никита',
            'Олег', 'Ольга', 'Федор']

selected_students = random.sample(students, 4)
print("имена студентов, которые будут отвечать на уроке:")

for student in selected_students:
    print(student)

for student in selected_students:
    students.remove(student)
