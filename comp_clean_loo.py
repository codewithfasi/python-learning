classrooms = [["sara", "ali"], ["omar", "mona"], ["noor", "yasir"]]
clean_classrooms = [
    [student.title() for student in classroom] for classroom in classrooms
]

print(clean_classrooms)
