course = {
    "title": "python basics",
    "duration": 30,
    "price": 500.0,
    "mode": "Online",
    "active": False,
    "trainer": "Ahmed",
}
print(course)
print(course["title"])
print(course["duration"])
print(course["price"])
print(course["trainer"])
# print(course["location"])
# This gives an error before adding location because "location" key does not exist.
course.update(
    {
        "title": "Python Advanced",
        "price": 750.0,
        "active": True,
        "location": "Riyadh",
        "level": "Intermediate",
        "category": "Programming",
    }
)
has_trainer = "trainer" in course
has_certificate = "certificate" in course
has_location = "location" in course
print("Training key exist:", has_trainer)
print("Certificate key exist:", has_certificate)
print("Location key exist:", has_location)
print(course.get("trainer"))
print(course.get("certificate"))
print(course.get("certificate", "No certificate available"))
print(course.get("location", "No location found"))
print(course.keys())
print(course.values())
print(course.items())
print(len(course))
course_copy = course.copy()
course_copy.update({"mode": "Offline", "price": 900.0})
print(course["mode"])
print(course_copy["mode"])
print(course["price"])
print(course_copy["price"])
course.setdefault("location", "Jeddah")
course.setdefault("certificate", "No certificate")
fields = ["student_name", "email", "phone", "course"]
registration_form = dict.fromkeys(fields, None)
print(registration_form)
registration_form.update(
    {
        "student_name": "Faisal Ali",
        "email": "faisal@gmail.com",
        "phone": "0551234567",
        "course": "Python Advanced",
    }
)
print(registration_form)
payment = dict(method="Cash", amount=750.0, paid=True)
print(payment)
course_codes = {("Python Advanced", "Riyadh"): "Available"}
print(course_codes[("Python Advanced", "Riyadh")])
students = {
    "student1": {"name": "Ali", "course": "Python Basics"},
    "student2": {"name": "Sara", "course": "HTML Basics"},
}
print(students["student2"]["course"])
students["student1"].update({"course": "Python Advanced", "city": "Riyadh"})
students["student2"].update({"city": "Jeddah"})
students["student1"].setdefault("email", "No email")
students["student2"].setdefault("email", "No email")
print(students)
students["student1"].update({"skills": ["Python", "HTML"]})
students["student1"]["skills"].append("CSS")
students["student1"]["skills"].extend(["Java", "SQL"])
removed_skill = students["student1"]["skills"].pop()
print(removed_skill)
print(students["student1"]["skills"])
removed_trainer = course.pop("trainer")
print(removed_trainer)
removed_pair = course.popitem()
print(removed_pair)
del course["active"]
print(course)
course.clear()
print(course)
