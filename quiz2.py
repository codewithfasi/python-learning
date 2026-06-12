student_name = "   sARA aHmed   "
age = "17"
marks = "84.5"
email = "  SARA@GMAIL.COM "
course = " python basics "
file_name = "certificate.PDF"
registered_students = ["Ali", "Omar", "Mona"]
waiting_students = ["Noor", "Faisal"]
blocked_students = ["Yasir", "Hamad"]
student_name = student_name.strip().title()
age = int(age)
marks = float(marks)
email = email.strip().lower()
course = course.strip().title()
file_name = file_name.strip().lower()
course_valid = course.startswith("Python")
print("Student Name:", student_name)
print("Student Age:", age)
print("Student Marks:", marks)
print("Student Email:", email)
print("Course:", course)
print("File:", file_name)
print("Course Valid:", course_valid)
email_valid = email.endswith("@gmail.com")
file_valid = file_name.endswith(".pdf")
passed = marks >= 80
is_adult = age >= 18
print("Email Valid:", email_valid)
print("Is File Valid:", file_valid)
print("Passed:", passed)
print("Adult:", is_adult)
if is_adult and passed and email_valid and file_valid:
    print("Student Fully Accepted")
elif not is_adult and passed:
    print("Underage but strong student")
elif not email_valid:
    print("Invalid email")
elif not file_valid:
    print("Invalid file")
else:
    print("Student rejected")
registered_students.append(student_name)
registered_students.extend(waiting_students)
registered_students.insert(1, "Admin Student")
registered_students.remove("Omar")
removed_student = registered_students.pop()
del registered_students[0]
print("Registered Students:", registered_students)
print("Removed Student:", removed_student)
print("Total Students:", len(registered_students))
if student_name in registered_students:
    print(student_name, "is registered")
else:
    print(student_name, "is not registered")
if student_name in blocked_students:
    print("Student is blocked")
else:
    print("Student is allowed")
print("First Student:", registered_students[0])
print("Last Student:", registered_students[-1])
print("First Two Students:", registered_students[:2])
print("Last two Stduents:", registered_students[-2:])
print("Students form index 1 to index 3:", registered_students[1:4])
