username = "Ali"
blocked = False
account_active = True
password_correct = True
email_verified = False
phone_verified = True
is_admin = False
has_dashboard_permission = True
login_attempts = 2
logged_in_other_device = False
if (
    not blocked
    and account_active
    and password_correct
    and (email_verified or phone_verified)
    and (is_admin or has_dashboard_permission)
    and 1 <= login_attempts <= 3
    and not logged_in_other_device
):
    print("Dashboard access allowed")
else:
    print("Dashboard access denied")


a = [1, 2, 3]
b = [1, 2]

print(a < b)