students = ["Sara", "Omar", "Ali", "Noor"]
scores = [92, 45, 80, 38]
for student, score in zip(students, scores):
    if score >= 50:
        print("Passed student:", student, "Score:", score)
