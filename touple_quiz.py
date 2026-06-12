students = (
    ("Ali", 85, "Lahore"),
    ("Sara", 92, "Islamabad"),
    ("Omar", 45, "Karachi"),
    ("Noor", 70, "Lahore"),
)
lahore_students = []
other_city_students = []
for name, score, city in students:
    if city.endswith("Lahore"):
        lahore_students.append(name)
    else:
        other_city_students.append(name)
print(lahore_students)
print(other_city_students)
