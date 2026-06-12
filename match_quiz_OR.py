role = "teacher"
match role:
    case "admin" | "manager":
        print("Full access")
    case "teacher" | "trainer":
        print("teaching access")
    case "student":
        print("Student access")
    case _:
        print("Unknown role")
