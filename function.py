def check_login_access(
    username,
    blocked,
    account_active,
    password_correct,
    email_verified,
    phone_verified,
    login_attempts,
    logged_in_other_device,
    accepted_terms,
):
    if (
        not blocked
        and account_active
        and password_correct
        and (email_verified or phone_verified)
        and 1 <= login_attempts <= 3
        and not logged_in_other_device
        and accepted_terms
    ):
        print(username, "login allowed")
    else:
        print(username, "login denied")


check_login_access("Ali", 75, False, True)
