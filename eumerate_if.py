files = ["cv.pdf", "photo.jpg", "report.pdf"]

for index, file in enumerate(files):
    if file.endswith(".pdf"):
        print("PDF found at index:", index)
        print("File name:", file)
