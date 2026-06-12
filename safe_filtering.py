courses = [" Python ", "java", " EMPTY ", " PYTHON", "html ", "python "]
python_courses = []
for course in courses:
    clean_course = course.strip().title()
    if clean_course == "Empty":
        continue
    if not clean_course == "Python":
        continue
    python_courses.append(clean_course)
print(python_courses)
