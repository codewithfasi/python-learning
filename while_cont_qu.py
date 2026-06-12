roll = 1
while roll <= 7:
    if roll == 3:
        print("Absent roll number skipped:", roll)
        roll = roll + 1
        continue
    if roll == 6:
        print("Absent roll number skipped:", roll)
        roll = roll + 1
        continue
    print("Checking roll number:", roll)
    roll = roll + 1
print("Roll number check completed")
