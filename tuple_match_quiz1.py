record = ("Sara", "completed")
match record:
    case (name, "completed"):
        print("Course completed by:", name)
    case (name, "pending"):
        print("Course pending for:", name)
    case _:
        print("Unknown course status")
