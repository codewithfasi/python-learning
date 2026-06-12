text = "Ali 123@"
letter_count = 0
space_count = 0
digit_count = 0
special_count = 0
for letter in text:
    if letter.isalpha():
        print(letter, "Letter")
        letter_count = letter_count + 1
    elif letter.isspace():
        print(letter, "Space")
        space_count = space_count + 1
    elif letter.isdigit():
        print(letter, "Digit")
        digit_count = digit_count + 1
    else:
        print(letter, "Special")
        special_count = special_count + 1
print("Total Letter:", letter_count)
print("Total Space:", space_count)
print("Total Digit:", digit_count)
print("Total Soecial:", special_count)
print("Text checking finished")
