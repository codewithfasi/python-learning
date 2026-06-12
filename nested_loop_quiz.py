students = [" Sara ", "EMPTY", " ali", " Omar ", " absent ", "Mona "]
courses = [" PYTHON ", "html", " EMPTY ", "Java ", " python"]
registrations = []
total_registrations = 0
for student in students:
    clean_student = student.strip().title()
    if clean_student == "Empty":
        continue
    if clean_student == "Absent":
        continue
    for course in courses:
        clean_course = course.strip().title()
        if clean_course == "Empty":
            continue
        if not clean_course == "Python":
            continue
        registrations.append((clean_student, clean_course))
        total_registrations = total_registrations + 1
print(registrations)
print(total_registrations)
