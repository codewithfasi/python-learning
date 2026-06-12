student = {
    "name": "Faisal",
    "age": 18,
    "course": "Python",
    "marks": 79.5,
    "email": "faisal@gmail.com",
    "passed": False,
}
print(student)
print(student["name"])
print(student["age"])
print(student["course"])
student["course"] = "Advanced python"
print(student["course"])
student["phone"] = "0551234567"
print(student["phone"])
has_email = "email" in student
has_address = "address" in student
print(has_email)
print(student.get("email"))
print(student.get("address"))
print(student.get("address", "No address found"))
print(student.keys())
print(student.values())
print(student.items())
removed_marks = student.pop("marks")
print(removed_marks)
print(student)
del student["passed"]
print(student)
student.clear()
print(student)
