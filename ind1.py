grades_str = input("Введите оценки учеников через пробел: ")
grades = tuple(map(int, grades_str.split()))

count_5 = grades.count(5)

print(f"Количество учеников с оценкой '5': {count_5}")
