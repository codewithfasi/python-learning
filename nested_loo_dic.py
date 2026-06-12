students = [
    {"name": "Sara", "courses": ["Python", "HTML"]},
    {"name": "Ali", "courses": ["Java"]}
]
for student in students:
    for course in student["courses"]:
        print(student["name"], course)