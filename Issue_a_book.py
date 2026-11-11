import json
def issue_a_book():
    with open("issued_books.json", "r") as f:
     with open("new_book.json", "r") as f:
        new_book = json.load(f)
    with open("new_student.json", "r") as f:
        new_student = json.load(f)
    l=input("enter student roll no: ")
    m=input("enter book id: ")

    def book_save_and_issue(student_id,book_id):
            if student_id not in new_student:
                print(f" student id{student_id} not in student database")
                return False

            if book_id not in new_book:
                print(f" book id{book_id} not in book database")
                return False
            remaining_copies = new_book.get("remaining_copies")
            issued_books = {}

            with open("issued_books.json", "w") as f:
                json.dump(issued_books, f, indent=4)
                a = input("enter student roll no: ")
                b = input("enter book id: ").strip()
                c = input("enter book name: ").strip()
                d = input("enter book author: ").strip()
                e = input("enter issue date: ").strip()
                issued_books[a] = {
                        "book id": b,
                    "book name": c,
                    "author": d,
                    "issue date": e,
                }

            print(issued_books)
            print(f"successfully issued {c} in {issued_books}")
            return True
    book_save_and_issue(l,m)
issue_a_book()
