available_courses = {"Python", "Java", "HTML"}
student_course = "CSS"
course_available = student_course in available_courses
print(course_available)
if course_available is True:
    print("Course is available")
else:
    print("Course is not available")
