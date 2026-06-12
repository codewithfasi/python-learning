files = [
    " CV.PDF ",
    "photo.jpg",
    " EMPTY ",
    " report.DOCX ",
    "virus.exe",
    " certificate.PDF ",
    "notes.txt"
]

file_status = [
    "Approved" if file.strip().lower().endswith(".pdf") or file.strip().lower().endswith(".docx") else "Rejected"
    for file in files
]

print(file_status)
