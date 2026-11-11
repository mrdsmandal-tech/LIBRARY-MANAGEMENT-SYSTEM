import json
with open("new_book.json", "r") as f:
    book = json.load(f)
with open("issued_books.json", "r") as f:
    issued_books = json.load(f)
def return_a_book():
    a=input("Enter a book id: ")
    b=input("Enter student id: ")

    for book in issued_books:
        if book["id"] == a and book["student_id"] == b:
            issued_books.remove(book)
            with open("new_book.json", "r") as f:
                new_book = json.load(f)

    for books in new_book:
        if books["id"] in issued_books:
            books["available copies"]+=1
            with open("new_book.json", "w") as f:
                json.dump(books, f)
            print("book successfully returned")
            return
        print("book not found")

return_a_book()