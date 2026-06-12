students = ["Sara", "Absent", "Omar", "Ali"]

for index, student in enumerate(students):
    if student == "Absent":
        continue

    print("Present student at index:", index, "Name:", student)
