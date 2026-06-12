emails = ("  ALI@gmail.COM ", "sara@yahoo.com", " OMAR@GMAIL.com ")
clean_emails = []
for email in emails:
    clean_email = email.strip().lower()
    clean_emails.append(clean_email)
print(clean_emails)
