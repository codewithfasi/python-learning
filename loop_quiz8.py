username = "Faisal_123@"
letter_count = 0
digit_count = 0
special_count = 0
for character in username:
    if character.isalpha():
        print(character, "Letter")
        letter_count = letter_count + 1
    elif character.isdigit():
        print(character, "Digit")
        digit_count = digit_count + 1
    else:
        print(character, "Special")
        special_count = special_count + 1
print("Total letters:", letter_count)
print("Total Digits:", digit_count)
print("Total soecial:", special_count)
print("Username checking finished")
