names = ["Ali", "Sara", "Omar", "Noor", "Ahmed"]
long_name_count = 0
short_name_count = 0
for name in names:
    if len(name) >= 4:
        print(name, "Long name")
        long_name_count = long_name_count + 1
    else:
        print(name, "Short name")
        short_name_count = short_name_count + 1
print("Total long names:", long_name_count)
print("Total short names:", short_name_count)       
