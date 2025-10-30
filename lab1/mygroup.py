groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    }
]

def filter_students_by_avg(groupmates):
    try:
        threshold = float(input("Введите средний балл для фильтрации: "))
    except ValueError:
        print("Ошибка: введите число.")
        return

    print(f"\nСтуденты со средним баллом выше {threshold}:")
    found = False

    for student in groupmates:
        avg_mark = sum(student["marks"]) / len(student["marks"])
        if avg_mark > threshold:
            print(f"{student['name']} {student['surname']} — средний балл: {avg_mark:.2f}")
            found = True

    if not found:
        print("Нет студентов, удовлетворяющих условию.")

filter_students_by_avg(groupmates)