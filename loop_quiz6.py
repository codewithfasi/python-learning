orders = [
    {"item": "  laptop ", "price": 2500, "paid": True, "country": "Saudi Arabia"},
    {"item": "mouse", "price": 80, "paid": False, "country": "Saudi Arabia"},
    {"item": "keyboard", "price": 150, "paid": True, "country": "UAE"},
    {"item": "monitor", "price": 700, "paid": True, "country": "Saudi Arabia"},
    {"item": "usb cable", "price": 25, "paid": True, "country": "Saudi Arabia"},
]
accepted_count = 0
rejected_count = 0
for order in orders:
    item = order["item"].strip().title()
    price = order["price"]
    paid = order["paid"]
    country = order["country"].strip().lower()
    paid_status = paid == True
    price_check = price >= 100
    country_check = country == "saudi arabia"
    if paid_status and price_check and country_check:
        print(item, "Accepted")
        accepted_count = accepted_count + 1
    else:
        print(item, "Rejected")
        rejected_count = rejected_count + 1
print("Total accepted", accepted_count)
print("Total rejected", rejected_count)
print("Order checking finished")
