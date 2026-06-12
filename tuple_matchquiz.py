order = ("Laptop", "paid")

match order:
    case (product, "paid"):
        print("Paid order:", product)
    case (product, "unpaid"):
        print("Unpaid order:", product)
    case _:
        print("Unknown order status")
