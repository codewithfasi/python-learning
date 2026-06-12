emails = [
    "ali@gmail.com",
    "sara@gmail.com",
    "ali@gmail.com",
    "omar@gmail.com",
    "sara@gmail.com",
]
unique_email = set(emails)
print(emails)
print(unique_email)
uniqueemail_list = list(unique_email)
print(uniqueemail_list)
blocked_students = {"Hamad", "Khalid", "Omar"}
student_name = "Khalid"
blocked = student_name in blocked_students
print(blocked)
if blocked is True:
    print("Student is blocked")
else:
    print("Student can register")
skills = {"Python", "HTML"}
new_skill = "CSS"
skills.add(new_skill)
print(skills)
new_skill_python = "Python"
skills.add(new_skill_python)
print(skills)
