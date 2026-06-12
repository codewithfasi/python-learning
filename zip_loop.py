students = ["Sara", "Omar", "Ali"]
scores = [90, 75, 88]
for student, score in zip(students, scores):
    print("Student:", student, "Score:", score)

products = ["Laptop", "Mouse", "Keyboard"]
stocks = [5, 0, 3]

for product, stock in zip(products, stocks):
    if stock > 0:
        print("Available product:", product, "Stock:", stock)
