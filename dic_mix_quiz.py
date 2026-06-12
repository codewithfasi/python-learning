student = {
    "name": "faisal",
    "age": 18,
    "course": "Python",
    "marks": 79.5,
    "email": "faisal@gmail.com",
    "passed": False,
}
print(student)
print(student["name"])
print(student["course"])
print(student["marks"])
print(student["email"])
# print(student["phone"])
# This gives an error before adding phone because "phone" key does not exist.
student.update({"name": "Faisal Ali", "course": "Advanced Python", "passed": True})
print(student)
print(student["name"], student["course"], student["passed"])
student.update({"phone": "0551234567", "city": "Riyadh", "level": "Beginner"})
print(student)
has_email = "email" in student
has_address = "address" in student
has_phone = "phone" in student
print("Email key exist:", has_email)
print("Phone key exist:", has_phone)
print("Address key exist:", has_address)
print(student.get("email"))
print(student.get("address"))
print(student.get("address", "No address found"))
print(student.get("phone", "No phone found"))
print(student.keys())
print(student.values())
print(student.items())
print(len(student))
student_copy = student.copy()
student_copy["course"] = "Data Analysis"
print(student["course"])
print(student_copy["course"])
student.update({"country": "Saudi Arabia", "level": "Intermediate", "status": "Active"})
print(student)
student.setdefault("city", "Jeddah")
student.setdefault("address", "No address")
print(student["city"])
print(student["address"])
fields = ["username", "password", "email"]
empty_form = dict.fromkeys(fields, None)
print(empty_form)
course_info = dict(title="Python Basics", duration=30, mode="online")
print(course_info)
student_codes = {("Faisal", 18): "Registered"}
print(student_codes[("Faisal", 18)])
students = {
    "student1": {"name": "Ali", "course": "Python"},
    "student2": {"name": "Sara", "course": "HTML"},
}
print(students["student2"]["course"])
students["student1"].update({"course": "Java"})
print(students["student1"]["course"])
students["student1"].update({"city": "Lahore"})
students["student2"].update({"city": "Jeddah"})
students["student1"].setdefault("email", "No email")
students["student2"].setdefault("email", "No email")
print(students)
students["student1"].update({"courses": ["Python", "HTML"]})
students["student1"]["courses"].append("CSS")
students["student1"]["courses"].extend(["Java", "SQL"])
students["student1"]["courses"].remove("HTML")
removed_course = students["student1"]["courses"].pop()
print(removed_course)
print(students["student1"]["courses"])
removed_marks = student.pop("marks")
print(removed_marks)
print(student)
removed_pair = student.popitem()
print(removed_pair)
print(student)
del student["passed"]
print(student)
student.clear()
print(student)
