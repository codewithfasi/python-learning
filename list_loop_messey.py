names = [" ali ", "SARA", "  omar", "no"]
short_name_count = 0
Long_name_count = 0
for name in names:
    name = name.strip().lower().title()
    if len(name) >= 4:
        print(name, "Long name")
        Long_name_count = Long_name_count + 1
    else:
        print(name, "Short name")
        short_name_count = short_name_count + 1
print("Total Long name:", Long_name_count)
print("Total short name:", short_name_count)
print("Name checking finished")
