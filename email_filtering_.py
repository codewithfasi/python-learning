emails = [" ali@gmail.com ", "SARA@yahoo.com", " omar@gmail.com ", "noor@hotmail.com"]
gmail_emails = []
other_emails = []
for email in emails:
    clean_email = email.strip().lower()
    if clean_email.endswith("@gmail.com"):
        gmail_emails.append(clean_email)
    else:
        other_emails.append(clean_email)

print("Gmail emails:", gmail_emails)
print("Other email:", other_emails)
print("Email filtering finished")