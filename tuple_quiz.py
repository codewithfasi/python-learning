course_info = ("Python Basics", "Beginner", 30, "Online")
available_courses = ("Python", "Java", "Python", "HTML", "CSS")
allowed_levels = ("Beginner", "Intermediate", "Advanced")
student_course = "Python"
student_level = "Beginner"
print("Course name:", course_info[0])
print("Course level:", course_info[1])
print("Course duration:", course_info[2])
print("Course mode:", course_info[3])
if student_course in available_courses:
    print("Course is available")
else:
    print("Course is not available")
if student_level in allowed_levels:
    print("Level is allowed")
else:
    print("Level is not allowed")
print("Python Count:", available_courses.count("Python"))
print("HTML position", available_courses.index("HTML"))
print("First Two Courses:", available_courses[:2])
print("Last Two Courses:", available_courses[-2:])
print("Courses from index 1 to 3:", available_courses[1:4])
available_courses = list(available_courses)
available_courses.append("JavaScript")
available_courses = tuple(available_courses)
print(available_courses)
