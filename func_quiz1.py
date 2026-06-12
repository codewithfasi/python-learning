def check_book_borrowing(
    student, blocked, library_card, book_available, already_borrowed
):
    if not blocked and library_card and book_available and already_borrowed < 3:
        print(student, "can borrow book")
    else:
        print(student, "cannot borrow book")


check_book_borrowing("Ali", False, True, True, 1)
check_book_borrowing("Sara", False, False, True, 0)
check_book_borrowing("Omar", True, True, True, 1)
check_book_borrowing("Mona", False, True, False, 2)
check_book_borrowing("Hamad", False, True, True, 3)
