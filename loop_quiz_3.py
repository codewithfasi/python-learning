emails = [
    "ali@gmail.com",
    "sara@yahoo.com",
    "omar@gmail.com",
    "noor@hotmail.com",
    "faisal@gmail.com",
]
valid_count = 0
invalid_count = 0
for email in emails:
    if email.endswith("@gmail.com"):
        print(email, "Valid")
        valid_count = valid_count + 1
    else:
        print(email, "Invalid")
        invalid_count = invalid_count + 1
print("Total valid", valid_count)
print("Total Invalid:", invalid_count)
print("Email checking finished")
