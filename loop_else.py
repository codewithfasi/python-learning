files = ["profile.jpg", "assignment.pdf", "notes.txt", "report.docx"]
counter = 0
checked_files = []
for file in files:
    counter = counter + 1
    checked_files.append(file)
    print("Checking file:", file)
    if file == "marksheet.pdf":
        print("Marksheet found")
        break
else:
    print("Marksheet not found")
print("Total files checked:", counter)
print("Checked files:", checked_files)
