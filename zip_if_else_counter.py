students = ["Sara", "Omar", "Ali", "Noor"]
scores = [90, 45, 80, 38]
passed_count = 0
failed_count = 0
for student, score in zip(students, scores):
    if score >= 50:
        passed_count = passed_count + 1
    else:
        failed_count = failed_count + 1
print("Passed count:", passed_count)
print("Failed count:", failed_count)
