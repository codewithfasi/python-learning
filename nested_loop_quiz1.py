students = [" Sara ", "EMPTY", " ali", " BLOCKED ", " Omar ", " absent ", "Mona "]

files = [
    " CV.PDF ",
    "photo.jpg",
    " EMPTY ",
    " report.docx",
    "virus.exe",
    " certificate.PDF ",
    "notes.txt",
]

approved_uploads = []
rejected_files = []

total_approved = 0
total_rejected = 0

for student in students:
    clean_student = student.strip().title()

    if clean_student == "Blocked":
        continue

    if clean_student == "Empty":
        continue

    if clean_student == "Absent":
        continue

    for file in files:
        clean_file = file.strip().lower()

        if clean_file == "empty":
            continue

        if clean_file.endswith(".exe"):
            rejected_files.append((clean_student, clean_file))
            total_rejected = total_rejected + 1
            continue

        if not clean_file.endswith(".pdf") and not clean_file.endswith(".docx"):
            continue

        approved_uploads.append((clean_student, clean_file))
        total_approved = total_approved + 1

print(approved_uploads)
print(rejected_files)
print(total_approved)
print(total_rejected)
