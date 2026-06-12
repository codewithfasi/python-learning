day = 1

while day <= 5:
    if day == 3:
        print("Maintenance day skipped")
        day = day + 1
        continue

    print("Checking day:", day)
    day = day + 1

print("Day check completed")