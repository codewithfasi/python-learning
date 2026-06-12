files = ["cv.pdf", "photo.jpg", "corrupt.docx", "report.pdf"]
for index, file in enumerate(files):
    if file.endswith(".docx"):
        print("Corrupt file found at index:", index)
        print("File name:", file)
        break