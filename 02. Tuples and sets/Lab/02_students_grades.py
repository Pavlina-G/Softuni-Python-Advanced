n = int(input())
students = {}

for i in range(n):
    student_info = tuple(input().split(' '))
    student, grade = student_info
    if student not in students:
        students[student] = [float(grade)]
    else:
        students[student].append(float(grade))

for student, grades in students.items():
    average_grade = sum(grades) / len(grades)
    print(f"{student} -> {' '.join(map(lambda x: f'{x:.2f}', grades))} (avg: {average_grade:.2f})")

