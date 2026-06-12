count = 1
while count <= 5:
    print("Checking attempt:", count)

    if count == 3:
        print("Correct PIN found")
        break
    count = count + 1
print("Login process stopped")
