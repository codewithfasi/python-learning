products = ["  Laptop  ", "OUT", " phone ", "   ", "Tablet", " out ", "Mouse"]
counter = 0
available_products = []
for product in products:
    clean_product = product.strip().title()
    if clean_product == "":
        print("Empty product skipped")
        continue
    if clean_product == "Out":
        print("Out of stock skipped")
        continue
    counter = counter + 1
    available_products.append(clean_product)
    print("Available product:", clean_product)
print("Total available products:", counter)
print("Available products:", available_products)



files = ["cv.pdf", "photo.jpg", "report.docx"]

for number, file in enumerate(files, start=1):
    print("File number:", number, "File name:", file)


files = ["cv.pdf", "photo.jpg", "report.pdf", "notes.txt"]

pdf_count = 0

for index, file in enumerate(files):
    if not file.endswith(".pdf"):
        continue

    pdf_count = pdf_count + 1
    print("PDF found at index:", index, "File name:", file)

print("Total PDF files:", pdf_count)

word = "Ali"

for index, letter in enumerate(word):
    print("Index:", index, "Letter:", letter)

password = "A1b"

for index, char in enumerate(password):
    print("Character index:", index, "Character:", char) 

courses = ("Python", "Java", "HTML")

for index, course in enumerate(courses):
    print("Course index:", index, "Course name:", course)

students = ["Sara", "Omar", "Ali"]

for index in range(len(students)):
    print("Index:", index, "Student:", students[index])  