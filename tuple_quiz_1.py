files = (" profile.JPG ", "notes.pdf", " image.jpg ", "DATA.CSV", "photo.JPG")
jpg_files = []
pdf_files = []
other_files = []
for file in files:
    clean_file = file.strip().lower()
    if clean_file.endswith(".jpg"):
        jpg_files.append(clean_file)
    elif clean_file.endswith(".pdf"):
        pdf_files.append(clean_file)
    else:
        other_files.append(clean_file)
print(jpg_files)
print(pdf_files)
print(other_files)
