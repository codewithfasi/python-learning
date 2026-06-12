order = {
    "order_id": "ORD1001",
    "student": "ali",
    "course": "HTML",
    "price": 150.0,
    "email": "ali@gmail.com",
    "paid": False,
}
print(order)
print(order["order_id"])
print(order["student"])
print(order["course"])
print(order["price"])
print(order["email"])
print(order["paid"])
# print(order["coupon"])
# This would give an error before adding coupon because the key does not exist.
order["student"] = "Ali Ahmed"
order["course"] = "Python Basics"
order["city"] = "Riyadh"
order["paid"] = True
print(order["student"])
print(order["course"])
print(order["paid"])
order["coupon"] = "PYTHON20"
order["discount"] = 20
has_email = "email" in order
has_coupon = "coupon" in order
has_phone = "phone" in order
print(has_email)
print(has_coupon)
print(has_phone)
print(order.get("email"))
print(order.get("phone", "No phone found"))
print(order.get("city", "No city found"))
print(order.keys())
print(order.values())
print(order.items())
remove_price = order.pop("price")
print(order)
del order["discount"]
print(order)
order["status"] = "confirmed"
print(order["status"])
order.clear()
print(order)
