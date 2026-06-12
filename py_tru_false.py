student_name = "   sArA   "
email = "   SARA@OUTLOOK.COM   "
course = "   python basics   "
blocked = False
age = 22
fee_paid = False
has_scholarship = True
clean_name = student_name.strip().title()
clean_email = email.strip().lower()
clean_course = course.strip().title()
if (
    not blocked
    and clean_course.startswith("Python")
    and 18 <= age <= 60
    and (
        clean_email.endswith("@gmail.com")
        or clean_email.endswith("@outlook.com")
        and (fee_paid or has_scholarship)
    )
):
    print("Allowed")
else:
    print("Not allowed")
