products = ["Mouse", "Monitor", "Keyboard", "Laptop", "Printer"]
counter = 0
checked_products = []
for product in products:
    counter = counter + 1
    checked_products.append(product)
    print("Checking product:", product)

    if product == "Keyboard":
        print("Keyboard found")
        break
else:
    print("Keyboard not found")

print("Total products checked:", counter)
print("Checked products:", checked_products)
print("Last checked product:", product)
