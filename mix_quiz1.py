student_name = "   fAiSaL aLi   "
age = "18"
marks = "79.5"
email = "  FAISAL@GMAIL.COM "
course = " python basics "
file_name = "PROFILE.JPG"
registered_students = ["Sara", "Omar", "Mona", "Sara"]
blocked_students = {"Hamad", "Khalid", "Faisal Ali"}
allowed_courses = ("Python Basics", "Java Basics", "HTML Basics")
allowed_extensions = {".jpg", ".png"}
student_name = student_name.strip().title()
age = int(age)
marks = float(marks)
email = email.strip().lower()
course = course.strip().title()
file_name = file_name.lower()
is_adult = age >= 18
passed = marks >= 80
email_valid = email.endswith("@gmail.com")
course_allowed = course in allowed_courses
blocked = student_name in blocked_students
file_valid = file_name.endswith(".jpg") or file_name.endswith(".png")
registered_students.append(student_name)
unique_students = set(registered_students)
print("Student Name:", student_name)
print("Age:", age)
print("Marks:", marks)
print("Email:", email)
print("Course:", course)
print("File_Name:", file_name)
print("Adult", is_adult)
print("Passed:", passed)
print("Email is valid:", email_valid)
print("Course allowed:", course_allowed)
print("File Valid:", file_valid)
if blocked:
    print("Student is blocked")
elif not is_adult:
    print("Student is under age")
elif not email_valid:
    print("Invalid email")
elif not course_allowed:
    print("Course not allowed")
elif not file_valid:
    print("Invalid file")
elif passed:
    print("Student accepted")
else:
    print("Student registered but did not pass")
# list methods
unique_students = set(registered_students)
student_list = list(unique_students)
student_list.append("Yasir")
student_list.append(["Noor", "Huda"])
student_list.insert(1, "Ziyad")
student_list.extend(["Lina", "Maha"])
student_list.remove("Omar")
popped_student = student_list.pop()
del student_list[0]
print(student_list)
print(popped_student)
student_list.remove(["Noor", "Huda"])
final_students_set = set(student_list)
final_students_set.add("Nasser")
final_students_set.update(["Ali", "Sara", "Yasir"])
print(final_students_set)
print(len(final_students_set))
studdent_tuple = tuple(student_list)
print(studdent_tuple[0])
print(studdent_tuple[-1])
print(studdent_tuple[1:3])
print(studdent_tuple.count("Sara"))
