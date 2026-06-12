classrooms = [
    ["Sara", "Ali"],
    ["Omar", "Mona"],
    ["Hamad"],
    ["Noor", "Yasir"]
]
counter = 0
for classroom in classrooms:
    for student in classroom:
        counter = counter + 1
        print(student)
print("Total Students:", counter)