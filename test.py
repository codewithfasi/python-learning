####join
names = ["  Ali", "Aisha", "Alia", "Sara   "]
update_name = " | ".join(names)
print(update_name)

student = {
    "name": "Faisal",
    "age": 18,
    "course": "Python",
    "marks": 79.5,
    "email": "faisal@gmail.com",
    "passed": False,
}
backup_student = student.copy()
backup_student["name"] = "yasir"
print(backup_student["name"])
backup_student.update({"name": "hasnain", "city": "Bahawalpur"})
print(backup_student)
print(backup_student["city"])

book = {"title": "Python", "price": 50, "author": "Sara"}

book["year"] = 2026

print(len(book))
