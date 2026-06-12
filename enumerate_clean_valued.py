students = [" sara ", " ABSENT ", " omar ", " ALI "]
for index, student in enumerate(students):
    clean_student = student.strip().title()
    if clean_student == "Absent":
        continue
    print("Present student at index:", index, "Student name:", clean_student)
