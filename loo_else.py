emails = [
    "  SARA@gmail.com  ",
    "OMAR@yahoo.com",
    " BLOCKED@gmail.com ",
    "ali@gmail.com",
    "noor@gmail.com",
]
counter = 0
checked_emails = []
for email in emails:
    clean_email = email.strip().lower()
    counter = counter + 1
    checked_emails.append(clean_email)
    print("Checking email:", clean_email)

    if clean_email == "blocked@gmail.com":
        print("Blocked email found")
        break
else:

    print("No blocked email found")
print("Total emails checked:", counter)
print("Checked emails:", checked_emails)
print("Last checked email:", clean_email)
