files = [" CV.PDF ", " photo.jpg ", " REPORT.PDF ", " notes.txt "]
pdf_files = []
for index, file in enumerate(files):
    clean_file = file.strip().lower()
    if not clean_file.endswith(".pdf"):
        continue
    pdf_files.append(clean_file)
print(pdf_files)