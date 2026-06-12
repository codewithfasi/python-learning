student_name = "Sara"
blocked = False
account_active = True
age = 21
score = 78
fee_paid = False
has_scholarship = True
email_verified = False
phone_verified = True
logged_in_other_device = False
if (
    not blocked
    and account_active
    and 18 <= age <= 60
    and 50 <= score <= 100
    and (fee_paid or has_scholarship)
    and (email_verified or phone_verified)
    and not logged_in_other_device
):
    print("Exam access allowed")
else:
    print("Exam access denied")
