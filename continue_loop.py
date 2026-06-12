counter = 0

students = ["Sara", "Absent", "Omar", "Ali"]

for student in students:
    counter = counter + 1

    if student == "Absent":
        continue

    print("Student:", student)

print("Total students:", counter)
