student_name = "   fAiSAL aLI   "
age = "18"
marks = "76.5"
email = "  FAISAL@YAHOO.COM "
course = " python basics "
file_name = "profile.JPG"

registered_students = ["Sara", "Omar", "Mona"]
waiting_students = ["Noor", "Yasir"]
blocked_students = ["Hamad", "Khalid"]

# Part 1: Clean data
student_name = student_name.strip().title()
age = int(age)
marks = float(marks)
email = email.strip().lower()
course = course.strip().title()
file_name = file_name.strip().lower()

print("Student Name:", student_name)
print("Age:", age)
print("Marks:", marks)
print("Email:", email)
print("Course:", course)
print("File name:", file_name)

# Part 2: Validation
email_valid = email.endswith("@gmail.com")
file_valid = file_name.endswith(".jpg")
course_valid = course.startswith("Python")
passed = marks >= 80
is_adult = age >= 18
blocked = student_name in blocked_students

print("Email is Valid:", email_valid)
print("File is valid:", file_valid)
print("Course is valid:", course_valid)
print("Passed:", passed)
print("Adult:", is_adult)
print("Blocked:", blocked)

# Part 3: Admission decision
if blocked:
    print("Student is blocked")
elif not email_valid:
    print("Invalid email provider")
elif not file_valid:
    print("Invalid profile image")
elif not course_valid:
    print("Invalid course")
elif is_adult and passed:
    print("Student fully accepted")
elif is_adult and marks >= 75:
    print("Student added to the waiting list")
else:
    print("Student rejected")

# Part 4: Update registered students list
registered_students.append(student_name)
registered_students.extend(waiting_students)
registered_students.insert(2, "Admin Student")
registered_students.remove("Omar")

removed_student = registered_students.pop(-1)

del registered_students[:2]

print("Registered student:", registered_students)
print("Removed Student:", removed_student)
print("Total Number of Student:", len(registered_students))

# Part 5: Check registration and blocked status
if student_name in registered_students:
    print(student_name, "is registered")
else:
    print(student_name, "is not registered")

if blocked:
    print("Student is blocked")
else:
    print("Student is allowed")

# Part 6: Indexing and slicing
print("First Student:", registered_students[0])
print("Last student:", registered_students[-1])
print("First two students:", registered_students[:2])
print("Last two students:", registered_students[-2:])
print("Students from index 1 to 3:", registered_students[1:4])

# Part 7: Copy, count, and index
backup_students = registered_students.copy()
backup_students.append("Backup Only Student")

print("Original Students:", registered_students)
print("Backup Students:", backup_students)

if "Backup Only Student" in registered_students:
    print("Backup student found in original")
else:
    print("Backup student only exists in backup")

mona_count = registered_students.count("Mona")
print("Mona Count:", mona_count)

if student_name in registered_students:
    student_index = registered_students.index(student_name)
    print("Student index:", student_index)
else:
    print("Student index not found")
