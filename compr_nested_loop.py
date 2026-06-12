classrooms = [
    ["Sara", "Ali"],
    ["Omar"],
    ["Mona", "Noor"],
    ["Hamad", "Yasir"]
]

all_students = [student for classroom in classrooms for student in classroom]

print(all_students)