courses = ("Python", "Java", "HTML")
clean_courses = []
for course in courses:
    clean_course = course.strip().title()
    clean_courses.append(clean_course)
print(clean_courses)
