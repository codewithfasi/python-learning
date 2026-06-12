fields = ["name", "age", "email"]
student = dict.fromkeys(fields, None)
print(student)
student.update({"name": "yasir", "email": "yasir@geo.tv"})
print(student)
student.setdefault("city", "Multan")
student.update({"age": 18})
print(student)
Multan = dict(city="punjab", weather=50, known="city of saints")
print(Multan)
#####nested dictionary
students = {
    "student1": {"name": "Ali", "course": "Python"},
    "student2": {"name": "Sara", "course": "HTML"},
}
students["student1"].update({"city": "lahore"})
students["student2"].update({"city": "Jeddah"})
students["student1"].setdefault("email", "No email")
students["student2"].setdefault("email", "No email")
print(students)
students["student1"].update({"courses": ["pyhton", "HTML"]})
print(students["student1"]["courses"])
students["student1"]["courses"].append("CSS")
print(students["student1"])
students["student1"]["courses"].extend(["Art", "pysics"])
print(students["student1"])
students["student1"]["courses"].extend(["Java", "SQL"])
print(students["student1"]["courses"])
fields = ["username", "password", "email"]
empty_form = fields.fromkeys(fields, None)
print(empty_form)
