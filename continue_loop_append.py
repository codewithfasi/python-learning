emails = [
    "  SARA@gmail.com  ",
    "omar@yahoo.com",
    "   ",
    "ALI@GMAIL.COM",
    "noor@hotmail.com",
    "yasir@gmail.com",
]
counter = 0
gmail_emails = []
for email in emails:
    clean_email = email.strip().lower()
    if clean_email == "":
        print("Empty email skipped")
        continue
    if not clean_email.endswith("@gmail.com"):
        print("Non-Gmail email skipped:",clean_email)
        continue
    counter = counter + 1
    gmail_emails.append(clean_email)
    print("Valid Gmail:", clean_email)
print("Total Gmail emails:", counter)
print("Gmail emails:", gmail_emails)
