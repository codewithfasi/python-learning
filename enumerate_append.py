students = ["Sara", "Absent", "Omar", "Ali"]
present_students = []
for index, student in enumerate(students):
    if student == "Absent":
        continue
    present_students.append(student)

print(present_students)
