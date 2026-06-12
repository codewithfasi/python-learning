file_type = "jpg"

match file_type:
    case "jpg" | "png" | "jpeg":
        print("Image file")
    case "pdf" | "docx":
        print("Document file")
    case _:
        print("Unknown file type")