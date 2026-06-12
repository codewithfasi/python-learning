classrooms = [
    ["sara", "ali"],
    ["omar"],
    ["mona", "noor"]
]
clean_classrooms = [
    [student.title() for student in classroom] for classroom in classrooms
    ]
print(clean_classrooms)