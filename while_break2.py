usernames = ["  sara  ", "OMAR", " ali ", " BLOCKED ", "noor", "yasir"]
count = 0
checked_users = []
while count < len(usernames):
    username = usernames[count]
    clean_username = username.strip().lower()

    checked_users.append(clean_username)
    print("Checking user:", clean_username)

    if clean_username == "blocked":
        print("Blocked user found")
        break
    count = count + 1

print("Total users checked:", len(checked_users))
print("Checked users:", checked_users)
print("Last checked user:", clean_username)
print("Security check stopped")
