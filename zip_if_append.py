products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
stocks = [5, 0, 3, 0]
available_products = []
out_of_stock_products = []
for product, stock in zip(products, stocks):
    if stock > 0:
        available_products.append(product)
    else:
        out_of_stock_products.append(product)

print(available_products)
print(out_of_stock_products)
