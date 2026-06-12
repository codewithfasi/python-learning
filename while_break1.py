passwords = [" wrong123 ", "HELLO", " Python123 ", "admin", "test123"]
count = 0
checked_passwords = []
while count < len(passwords):
    password = passwords[count]
    clean_password = password.strip().lower()

    checked_passwords.append(clean_password)
    print("Checking password:", clean_password)

    if clean_password == "python123":
        print("Correct password found")
        break
    count = count + 1

print("Total passwords checked:", len(checked_passwords))
print("Checked passwords:", checked_passwords)
print("Last checked password:", clean_password)
print("Login process stopped")
