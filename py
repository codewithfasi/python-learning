shop = 1
while shop <= 6:
    if shop == 4:
        print("Closed shop skipped")
        shop = shop + 1
        continue
    print("Checking shop:", shop)
    shop = shop + 1
print("Shop check completed")
