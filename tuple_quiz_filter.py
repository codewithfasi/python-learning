emails = ("  ALI@gmail.COM ", "sara@yahoo.com", " OMAR@GMAIL.com ", "noor@hotmail.com")
gmail_emails = []
other_emails = []
for email in emails:
    clean_email = email.strip().lower()
    if clean_email.endswith("@gmail.com"):
        gmail_emails.append(clean_email)
    else:
        other_emails.append(clean_email)
print(gmail_emails)
print(other_emails)
