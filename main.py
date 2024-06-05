
import random

students = {
    'male': ['Алексей', 'Артём', 'Борис', 'Владимир', 'Григорий', 'Дмитрий', 'Евгений', 'Игорь', 'Кирилл', 'Константин', 'Лев', 'Максим', 'Михаил', 'Никита', 'Олег', 'Федор'],
    'female': ['Анна', 'Антонина', 'Вероника', 'Елена', 'Ирина', 'Мария', 'Наталья', 'Ольга']
}

selected_students = random.sample(students['male'], 2) + random.sample(students['female'], 2)
print("имена студентов, которые будут отвечать на уроке:")

for student in selected_students:
    print(student)

for student in selected_students:
    if student in students['male']:
        students['male'].remove(student)
    elif student in students['female']:
        students['female'].remove(student)

print("\nоставшиеся студенты после отбора:")
for gender in students:
    for student in students[gender]:
        print(student)


