students = [
    {
        "name": "  ali  ",
        "age": 19,
        "email": "ALI@gmail.com",
        "course": " python basics ",
        "file": "photo.JPG",
    },
    {
        "name": "sara",
        "age": 17,
        "email": "sara@yahoo.com",
        "course": "python basics",
        "file": "cv.pdf",
    },
    {
        "name": "omar",
        "age": 22,
        "email": "omar@gmail.com",
        "course": "java basics",
        "file": "profile.jpg",
    },
    {
        "name": "noor",
        "age": 20,
        "email": "noor@gmail.com",
        "course": "python advanced",
        "file": "image.jpg",
    },
    {
        "name": "khalid",
        "age": 25,
        "email": "khalid@gmail.com",
        "course": "python basics",
        "file": "photo.jpg",
    },
]

blocked_students = ["Khalid", "Hamad"]
approved_count = 0
rejected_count = 0
for student in students:
    name = student["name"].strip().title()
    email = student["email"].strip().lower()
    course = student["course"].strip().lower()
    file = student["file"].strip().lower()
    age = student["age"]
    email_valid = email.endswith("@gmail.com")
    file_valid = file.endswith(".jpg")
    course_valid = course.startswith("python")
    is_adult = age >= 18
    blocked = name in blocked_students
    if email_valid and file_valid and course_valid and is_adult and not blocked:
        print(name, "Approved")
        approved_count = approved_count + 1
    else:
        print(name, "Rejected")
        rejected_count = rejected_count + 1
print("Total Aproved:", approved_count)
print("Total Rejected:", rejected_count)
print("Admission checking finished")
