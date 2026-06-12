courses = [" python ", "HTML", "  css", "java  "]
cleaned_courses = []
for course in courses:
    clean_course = course.strip().title()
    cleaned_courses.append(clean_course)
print(cleaned_courses)
print(courses)
print("Course cleaning finished")
