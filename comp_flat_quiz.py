student_files = [
    ["cv.pdf", "photo.jpg"],
    ["report.docx"],
    ["certificate.pdf", "notes.txt"]
]
all_files = [file for file in student_files for file in student_files]
print(all_files)

