file_type = "pdf"

match file_type:
    case "pdf":
        print("PDF file detected")
    case "jpg":
        print("Image file detected")
    case "docx":
        print("Word document detected")
    case _:
        print("Unknown file type")
