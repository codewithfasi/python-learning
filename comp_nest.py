student_files = [
    ["cv.pdf", "photo.jpg"],
    ["report.docx"],
    ["certificate.pdf", "notes.txt"],
    ["marksheet.pdf", "id.png"],
]
all_files = [file for student_file in student_files for file in student_file]
print(all_files)
