book = {
    "book_id": "BK2026",
    "title": "python basics",
    "author": "John Smith",
    "price": 45.5,
    "available": True,
    "category": "Programming",
}
print(book)
print(book["book_id"])
print(book["title"])
print(book["author"])
print(book["price"])
# print(book["publisher"])
# This would give an error before adding publisher because the key does not exist.
book["title"] = "Python Basics"
book["price"] = 50.0
book["available"] = False
book["publisher"] = "Code House"
book["year"] = 2026
book["language"] = "English"
print(book["title"])
print(book["price"])
print(book["available"])
print(book)
has_author = "author" in book
has_publisher = "publisher" in book
has_discount = "discount" in book
print(has_author)
print(has_publisher)
print(has_discount)
print(book.get("author"))
print(book.get("discount"))
print(book.get("discount", "No discount found"))
print(book.get("language", "No language found"))
print(book.keys())
print(book.values())
print(book.items())
removed_price = book.pop("price")
print(removed_price)
print(book)
del book["available"]
print(book)
book.clear()
print(book)
