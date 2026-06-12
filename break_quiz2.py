files = ["profile.jpg", "assignment.pdf", "damaged.docx", "notes.txt", "report.pdf"]
for file in files:
    print("Checking file:", file)
    if file == "damaged.docx":
        print("Damaged file found")
        break
