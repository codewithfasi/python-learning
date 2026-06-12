student_names = [" Sara ", "EMPTY", " ali", " BLOCKED ", "Omar ", "", " Mona "]

emails = [
    " ALI@GMAIL.COM ",
    " sara@yahoo.com ",
    " EMPTY ",
    " OMAR@GMAIL.COM ",
    " noor@hotmail.com ",
    " MONA@GMAIL.COM ",
]

scores = [45, 80, 90, 30, 75, 100]

files = [
    " CV.PDF ",
    "photo.jpg",
    " EMPTY ",
    " report.DOCX ",
    "virus.exe",
    " certificate.PDF ",
    "notes.txt",
]
valid_students = [
    student_name.strip().title()
    for student_name in student_names
    if student_name.strip().title() != ""
    and student_name.strip().title() != "Empty"
    and student_name.strip().title() != "Blocked"
]
gmail_emails = [
    email.strip().lower()
    for email in emails
    if email.strip().lower() != "empty" and email.strip().lower().endswith("@gmail.com")
]
passed_scores = [score for score in scores if score >= 50]

approved_files = [
    file.strip().lower()
    for file in files
    if file.strip().lower() != "empty"
    and file.strip().lower().endswith(".pdf")
    or file.strip().lower().endswith(".docx")
]
print(valid_students)
print(gmail_emails)
print(passed_scores)
print(approved_files)
