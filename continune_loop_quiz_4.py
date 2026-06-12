files = [
    " report.PDF ",
    "image.jpg",
    "   ",
    "notes.pdf",
    "data.xlsx",
    " assignment.PDF ",
]
counter = 0
pdf_files = []
for file in files:
    clean_file = file.strip().lower()
    if clean_file == "":
        # print("Empty file skipped") empty space check
        continue
    if not clean_file.endswith(".pdf"):
        # print("Non-PDF file skipped:", clean_file) invalid file check
        continue
    counter = counter + 1
    pdf_files.append(clean_file)
    print("Valid PDF:", clean_file)
print("Total PDF files:", counter)
print("PDF files:", pdf_files)
