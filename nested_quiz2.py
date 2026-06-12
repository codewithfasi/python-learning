schools = [
    [
        ["Sara", "Ali"],
        ["Omar"]
    ],
    [
        ["Mona", "Noor"],
        ["Hamad", "Yasir"]
    ]
]
counter = 0
for school in schools:
    for classroom in school:
        for student in classroom:
            counter = counter + 1
            print(student)
print("Total Number of students:", counter)
