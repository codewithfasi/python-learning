username = "Omar"
blocked = False
account_active = True
password_correct = True
email_verified = False
phone_verified = True
login_attempts = 2
logged_in_other_device = False
is_admin = False
accepted_terms = True

if (
    not blocked
    and account_active
    and password_correct
    and (email_verified or phone_verified)
    and 1 <= login_attempts <= 3
    and logged_in_other_device
    and (is_admin or accepted_terms)
):
    print("Login allowed")
else:
    print("Login denied")
